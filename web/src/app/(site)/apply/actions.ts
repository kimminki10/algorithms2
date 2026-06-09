"use server";

import { redirect } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { getSession } from "@/lib/auth";
import { APP_TYPES, ACTIVE_BOOKING_STATUS, type AppType } from "@/lib/constants";

export async function submitApplication(formData: FormData) {
  const type = String(formData.get("type") || "").toUpperCase();
  if (!(type in APP_TYPES)) throw new Error("잘못된 신청 유형입니다.");

  const user = await getSession();

  const facility = String(formData.get("facility") || "").trim() || null;
  const timeSlot = String(formData.get("timeSlot") || "").trim() || null;
  const desiredDate = String(formData.get("desiredDate") || "").trim() || null;

  // 대관: 동일 시설·날짜·시간대 중복 예약 방지 (서버 측 최종 검증)
  if (type === "RENTAL") {
    if (!facility || !desiredDate || !timeSlot) {
      redirect(`/apply/rental?error=incomplete`);
    }
    const conflict = await prisma.application.findFirst({
      where: { type: "RENTAL", facility, desiredDate, timeSlot, status: { in: ACTIVE_BOOKING_STATUS } },
    });
    if (conflict) {
      redirect(`/apply/rental?error=conflict`);
    }
  }

  await prisma.application.create({
    data: {
      type: type as AppType,
      title: String(formData.get("title") || "").trim(),
      applicantName: String(formData.get("applicantName") || "").trim(),
      phone: String(formData.get("phone") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      desiredDate,
      facility,
      timeSlot,
      content: String(formData.get("content") || "").trim(),
      userId: user?.id ?? null,
    },
  });

  redirect(`/apply/${type.toLowerCase()}?submitted=1`);
}
