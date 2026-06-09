import Link from "next/link";
import { PageHero, Section } from "@/components/ui";
import { APP_TYPES } from "@/lib/constants";

export const metadata = { title: "신청" };

export default function ApplyPage() {
  return (
    <>
      <PageHero crumb="APPLY" title="온라인 신청" subtitle="원하시는 신청 유형을 선택하세요." />
      <Section>
        <div className="grid gap-5 md:grid-cols-3">
          {(Object.keys(APP_TYPES) as (keyof typeof APP_TYPES)[]).map((key) => {
            const t = APP_TYPES[key];
            return (
              <Link
                key={key}
                href={`/apply/${key.toLowerCase()}`}
                className="group rounded-2xl border border-slate-200 bg-white p-8 transition hover:-translate-y-1 hover:border-brand-200 hover:shadow-lg"
              >
                <div className="grid h-14 w-14 place-items-center rounded-2xl bg-brand-50 text-3xl">{t.icon}</div>
                <h3 className="mt-5 text-xl font-bold text-slate-900">{t.label}</h3>
                <p className="mt-2 text-sm text-slate-500">{t.desc}</p>
                <span className="mt-6 inline-flex items-center gap-1 font-bold text-brand-600">
                  신청서 작성 <span className="transition group-hover:translate-x-1">→</span>
                </span>
              </Link>
            );
          })}
        </div>
      </Section>
    </>
  );
}
