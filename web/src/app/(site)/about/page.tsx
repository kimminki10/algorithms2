import { PageHero, Section } from "@/components/ui";
import { SITE } from "@/lib/constants";

export const metadata = { title: "기관소개" };

const stats = [
  { n: "12,000+", l: "연간 이용자" },
  { n: "350+", l: "운영 프로그램" },
  { n: "8", l: "대관 시설" },
  { n: "15년", l: "운영 경력" },
];

const values = [
  { icon: "🤝", t: "함께", d: "지역 주민과 기관이 함께 만들어가는 열린 공간을 지향합니다." },
  { icon: "🌱", t: "성장", d: "다양한 교육·프로그램으로 개인과 지역의 성장을 돕습니다." },
  { icon: "💡", t: "혁신", d: "온라인 신청 등 편리한 서비스로 더 나은 경험을 제공합니다." },
];

export default function AboutPage() {
  return (
    <>
      <PageHero crumb="ABOUT" title="기관소개" subtitle={`${SITE.name}는 ${SITE.tagline}를 비전으로 합니다.`} />
      <Section>
        <div className="rounded-2xl border border-slate-200 bg-white p-8">
          <h2 className="text-xl font-extrabold text-slate-900">인사말</h2>
          <p className="mt-4 leading-8 text-slate-600">
            안녕하세요. {SITE.name}를 찾아주신 여러분을 진심으로 환영합니다. 저희 센터는 지역 사회의 다양한
            요구에 부응하여 시설 대관, 교육 프로그램, 지원사업 등 폭넓은 서비스를 제공하고 있습니다.
            앞으로도 주민 여러분께 신뢰받는 열린 공간이 되도록 최선을 다하겠습니다.
          </p>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-4 md:grid-cols-4">
          {stats.map((s) => (
            <div key={s.l} className="rounded-2xl border border-slate-200 bg-white p-6 text-center">
              <div className="text-2xl font-extrabold text-brand-600">{s.n}</div>
              <div className="mt-1 text-sm text-slate-500">{s.l}</div>
            </div>
          ))}
        </div>

        <h2 className="mt-12 text-xl font-extrabold text-slate-900">핵심 가치</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {values.map((v) => (
            <div key={v.t} className="rounded-2xl border border-slate-200 bg-white p-6">
              <div className="text-3xl">{v.icon}</div>
              <h3 className="mt-3 text-lg font-bold text-slate-900">{v.t}</h3>
              <p className="mt-1 text-sm text-slate-500">{v.d}</p>
            </div>
          ))}
        </div>

        <h2 className="mt-12 text-xl font-extrabold text-slate-900">오시는 길</h2>
        <div className="mt-4 grid gap-4 rounded-2xl border border-slate-200 bg-white p-6 md:grid-cols-3">
          <div><p className="text-sm font-semibold text-slate-400">주소</p><p className="mt-1 font-semibold">{SITE.address}</p></div>
          <div><p className="text-sm font-semibold text-slate-400">전화</p><p className="mt-1 font-semibold">{SITE.tel}</p></div>
          <div><p className="text-sm font-semibold text-slate-400">이메일</p><p className="mt-1 font-semibold">{SITE.email}</p></div>
        </div>
      </Section>
    </>
  );
}
