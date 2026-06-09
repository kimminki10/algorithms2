import Link from "next/link";
import { notFound } from "next/navigation";
import { PageHero, Section, Button, Field } from "@/components/ui";
import { APP_TYPES, type AppType } from "@/lib/constants";
import { getSession } from "@/lib/auth";
import { submitApplication } from "../actions";

export default async function ApplyFormPage({
  params,
  searchParams,
}: {
  params: Promise<{ type: string }>;
  searchParams: Promise<{ submitted?: string }>;
}) {
  const { type } = await params;
  const { submitted } = await searchParams;
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

          {key === "RENTAL" && (
            <Field label="희망 일자" name="desiredDate" type="date" required />
          )}

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
