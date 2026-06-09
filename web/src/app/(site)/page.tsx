import Link from "next/link";
import { prisma } from "@/lib/prisma";
import { SITE, APP_TYPES } from "@/lib/constants";
import { Button } from "@/components/ui";

export default async function HomePage() {
  const notices = await prisma.notice.findMany({
    orderBy: [{ pinned: "desc" }, { createdAt: "desc" }],
    take: 5,
  });

  return (
    <>
      {/* Hero */}
      <section className="relative overflow-hidden bg-gradient-to-br from-brand-700 via-brand-600 to-brand-500 text-white">
        <div className="pointer-events-none absolute -right-24 -top-24 h-96 w-96 rounded-full bg-white/10 blur-2xl" />
        <div className="mx-auto max-w-6xl px-5 py-24">
          <p className="font-semibold tracking-wide text-brand-100">{SITE.tagline}</p>
          <h1 className="mt-3 max-w-3xl text-4xl font-extrabold leading-tight tracking-tight md:text-5xl">
            {SITE.name}에<br />오신 것을 환영합니다
          </h1>
          <p className="mt-5 max-w-xl text-lg text-brand-100">
            시설 대관부터 교육 프로그램, 지원사업 신청까지. 필요한 서비스를 온라인으로 간편하게 신청하세요.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button href="/apply" className="bg-white text-brand-700 hover:bg-brand-50">
              온라인 신청하기
            </Button>
            <Button href="/about" variant="outline" className="border-white/40 text-white hover:bg-white/10">
              기관 소개 보기
            </Button>
          </div>
        </div>
      </section>

      {/* Quick apply cards */}
      <section className="mx-auto -mt-10 max-w-6xl px-5">
        <div className="grid gap-4 md:grid-cols-3">
          {(Object.keys(APP_TYPES) as (keyof typeof APP_TYPES)[]).map((key) => {
            const t = APP_TYPES[key];
            return (
              <Link
                key={key}
                href={`/apply/${key.toLowerCase()}`}
                className="group rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:border-brand-200 hover:shadow-lg"
              >
                <div className="grid h-12 w-12 place-items-center rounded-xl bg-brand-50 text-2xl">{t.icon}</div>
                <h3 className="mt-4 text-lg font-bold text-slate-900">{t.label}</h3>
                <p className="mt-1 text-sm text-slate-500">{t.desc}</p>
                <span className="mt-4 inline-flex items-center gap-1 text-sm font-bold text-brand-600">
                  신청하기 <span className="transition group-hover:translate-x-1">→</span>
                </span>
              </Link>
            );
          })}
        </div>
      </section>

      {/* Latest notices */}
      <section className="mx-auto max-w-6xl px-5 py-16">
        <div className="flex items-end justify-between">
          <div>
            <h2 className="text-2xl font-extrabold text-slate-900">공지사항</h2>
            <p className="mt-1 text-slate-500">센터의 새로운 소식을 확인하세요.</p>
          </div>
          <Link href="/notices" className="text-sm font-bold text-brand-600 hover:underline">
            전체보기 →
          </Link>
        </div>

        <ul className="mt-6 divide-y divide-slate-100 rounded-2xl border border-slate-200 bg-white">
          {notices.length === 0 && (
            <li className="px-6 py-8 text-center text-slate-400">등록된 공지가 없습니다.</li>
          )}
          {notices.map((n) => (
            <li key={n.id}>
              <Link href={`/notices/${n.id}`} className="flex items-center gap-4 px-6 py-4 hover:bg-slate-50">
                {n.pinned && (
                  <span className="rounded bg-rose-100 px-2 py-0.5 text-xs font-bold text-rose-600">중요</span>
                )}
                <span className="flex-1 truncate font-semibold text-slate-800">{n.title}</span>
                <span className="text-sm text-slate-400">
                  {new Date(n.createdAt).toLocaleDateString("ko-KR")}
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </section>
    </>
  );
}
