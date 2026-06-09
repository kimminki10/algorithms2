"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { getSession } from "@/lib/auth";

async function requireAdmin() {
  const user = await getSession();
  if (!user || user.role !== "ADMIN") throw new Error("권한이 없습니다.");
  return user;
}

/* ---------- Applications ---------- */
export async function updateApplicationStatus(formData: FormData) {
  await requireAdmin();
  const id = String(formData.get("id"));
  const status = String(formData.get("status"));
  const adminNote = String(formData.get("adminNote") || "").trim() || null;
  await prisma.application.update({ where: { id }, data: { status, adminNote } });
  revalidatePath("/admin/applications");
}

/* ---------- Notices ---------- */
export async function createNotice(formData: FormData) {
  const admin = await requireAdmin();
  await prisma.notice.create({
    data: {
      title: String(formData.get("title") || "").trim(),
      content: String(formData.get("content") || "").trim(),
      pinned: formData.get("pinned") === "on",
      authorId: admin.id,
    },
  });
  revalidatePath("/admin/notices");
  revalidatePath("/notices");
  redirect("/admin/notices");
}

export async function updateNotice(formData: FormData) {
  await requireAdmin();
  const id = String(formData.get("id"));
  await prisma.notice.update({
    where: { id },
    data: {
      title: String(formData.get("title") || "").trim(),
      content: String(formData.get("content") || "").trim(),
      pinned: formData.get("pinned") === "on",
    },
  });
  revalidatePath("/admin/notices");
  revalidatePath("/notices");
  redirect("/admin/notices");
}

export async function deleteNotice(formData: FormData) {
  await requireAdmin();
  await prisma.notice.delete({ where: { id: String(formData.get("id")) } });
  revalidatePath("/admin/notices");
  revalidatePath("/notices");
}

/* ---------- FAQ ---------- */
export async function createFaq(formData: FormData) {
  await requireAdmin();
  await prisma.faq.create({
    data: {
      category: String(formData.get("category") || "일반").trim(),
      question: String(formData.get("question") || "").trim(),
      answer: String(formData.get("answer") || "").trim(),
    },
  });
  revalidatePath("/admin/faq");
  revalidatePath("/faq");
}

export async function deleteFaq(formData: FormData) {
  await requireAdmin();
  await prisma.faq.delete({ where: { id: String(formData.get("id")) } });
  revalidatePath("/admin/faq");
  revalidatePath("/faq");
}
