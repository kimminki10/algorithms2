"use server";

import { redirect } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { getSession } from "@/lib/auth";
import { APP_TYPES, type AppType } from "@/lib/constants";

export async function submitApplication(formData: FormData) {
  const type = String(formData.get("type") || "").toUpperCase();
  if (!(type in APP_TYPES)) throw new Error("잘못된 신청 유형입니다.");

  const user = await getSession();

  await prisma.application.create({
    data: {
      type: type as AppType,
      title: String(formData.get("title") || "").trim(),
      applicantName: String(formData.get("applicantName") || "").trim(),
      phone: String(formData.get("phone") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      desiredDate: String(formData.get("desiredDate") || "").trim() || null,
      content: String(formData.get("content") || "").trim(),
      userId: user?.id ?? null,
    },
  });

  redirect(`/apply/${type.toLowerCase()}?submitted=1`);
}
