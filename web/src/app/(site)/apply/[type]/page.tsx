import Link from "next/link";
import { notFound } from "next/navigation";
import { PageHero, Section, Button, Field } from "@/components/ui";
import { APP_TYPES, ACTIVE_BOOKING_STATUS, type AppType } from "@/lib/constants";
import { getSession } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { submitApplication } from "../actions";
import RentalForm from "@/components/RentalForm";

export default async function ApplyFormPage({
  params,
  searchParams,
}: {
  params: Promise<{ type: string }>;
  searchParams: Promise<{ submitted?: string; error?: string }>;
}) {
  const { type } = await params;
  const { submitted, error } = await searchParams;
  const key = type.toUpperCase() as AppType;
  if (!(key in APP_TYPES)) notFound();

  const meta = APP_TYPES[key];
  const user = await getSession();

  if (submitted) {
    return (
      <>
        <PageHero crumb="APPLY" title={meta.label} />
        <Section className="max-w-xl">
          <div className="rounded-2xl border border-emerald-200 bg-emerald-50 p-10 text-center">
            <div className="mx-auto grid h-16 w-16 place-items-center rounded-full bg-emerald-500 text-3xl text-white">✓</div>
            <h2 className="mt-5 text-xl font-extrabold text-slate-900">신청이 접수되었습니다</h2>
            <p className="mt-2 text-slate-600">
              담당자 확인 후 기재해 주신 연락처로 안내드리겠습니다.
              {user && " 신청 현황은 마이페이지에서 확인할 수 있습니다."}
            </p>
            <div className="mt-6 flex justify-center gap-3">
              <Button href="/" variant="outline">홈으로</Button>
              {user ? <Button href="/mypage">신청 현황 보기</Button> : <Button href="/apply">다른 신청하기</Button>}
            </div>
          </div>
        </Section>
      </>
    );
  }

  const errorMsg =
    error === "conflict"
      ? "선택하신 시설·날짜·시간대는 방금 다른 신청자가 예약했습니다. 다른 시간대를 선택해 주세요."
      : error === "incomplete"
      ? "시설·날짜·시간대를 모두 선택해 주세요."
      : null;

  // 대관: 달력 기반 예약 폼
  if (key === "RENTAL") {
    const active = await prisma.application.findMany({
      where: { type: "RENTAL", status: { in: ACTIVE_BOOKING_STATUS } },
      select: { facility: true, desiredDate: true, timeSlot: true },
    });
    return (
      <>
        <PageHero crumb="APPLY" title={meta.label} subtitle="시설과 날짜·시간대를 선택하면 예약 가능 여부가 실시간으로 표시됩니다." />
        <Section className="max-w-3xl">
          <Link href="/apply" className="text-sm font-bold text-brand-600 hover:underline">← 신청 유형 선택</Link>
          {errorMsg && (
            <p className="mt-4 rounded-xl bg-rose-50 px-4 py-3 text-sm font-semibold text-rose-600">{errorMsg}</p>
          )}
          <div className="mt-5">
            <RentalForm bookings={active} defaultName={user?.name} defaultEmail={user?.email} />
          </div>
        </Section>
      </>
    );
  }

  // 프로그램·사업: 기본 폼
  return (
    <>
      <PageHero crumb="APPLY" title={meta.label} subtitle={meta.desc} />
      <Section className="max-w-2xl">
        <Link href="/apply" className="text-sm font-bold text-brand-600 hover:underline">← 신청 유형 선택</Link>

        <form action={submitApplication} className="mt-5 space-y-5 rounded-2xl border border-slate-200 bg-white p-8">
          <input type="hidden" name="type" value={key} />

          <Field label="제목" name="title" required placeholder={`${meta.label} 제목을 입력하세요`} />

          <div className="grid gap-5 sm:grid-cols-2">
            <Field label="신청자명" name="applicantName" required defaultValue={user?.name} />
            <Field label="연락처" name="phone" required placeholder="010-0000-0000" />
          </div>
          <Field label="이메일" name="email" type="email" required defaultValue={user?.email} />

          <Field
            label="상세 내용"
            name="content"
            textarea
            required
            placeholder="신청 목적, 인원, 요청사항 등을 자세히 적어주세요."
          />

          <div className="flex items-center justify-between pt-2">
            <p className="text-xs text-slate-400">* 표시는 필수 입력 항목입니다.</p>
            <Button type="submit">신청서 제출</Button>
          </div>
        </form>
      </Section>
    </>
  );
}
