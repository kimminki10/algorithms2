"use server";

import { redirect } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { verifyPassword, hashPassword, createSession } from "@/lib/auth";

export async function login(_prev: unknown, formData: FormData) {
  const email = String(formData.get("email") || "").trim().toLowerCase();
  const password = String(formData.get("password") || "");
  const next = String(formData.get("next") || "/") || "/";

  const user = await prisma.user.findUnique({ where: { email } });
  if (!user || !(await verifyPassword(password, user.password))) {
    return { error: "이메일 또는 비밀번호가 올바르지 않습니다." };
  }

  await createSession({
    id: user.id,
    email: user.email,
    name: user.name,
    role: user.role as "USER" | "ADMIN",
  });
  redirect(next);
}

export async function signup(_prev: unknown, formData: FormData) {
  const name = String(formData.get("name") || "").trim();
  const email = String(formData.get("email") || "").trim().toLowerCase();
  const phone = String(formData.get("phone") || "").trim();
  const password = String(formData.get("password") || "");

  if (!name || !email || password.length < 6) {
    return { error: "이름, 이메일, 6자 이상 비밀번호를 입력해주세요." };
  }

  const exists = await prisma.user.findUnique({ where: { email } });
  if (exists) return { error: "이미 가입된 이메일입니다." };

  const user = await prisma.user.create({
    data: { name, email, phone, password: await hashPassword(password) },
  });

  await createSession({ id: user.id, email: user.email, name: user.name, role: "USER" });
  redirect("/");
}
