import { prisma } from "@/lib/prisma";
import { PageHero, Section } from "@/components/ui";

export const metadata = { title: "FAQ" };

export default async function FaqPage() {
  const faqs = await prisma.faq.findMany({ orderBy: [{ category: "asc" }, { sort: "asc" }] });

  const grouped = faqs.reduce<Record<string, typeof faqs>>((acc, f) => {
    (acc[f.category] ||= []).push(f);
    return acc;
  }, {});

  return (
    <>
      <PageHero crumb="FAQ" title="자주 묻는 질문" subtitle="궁금한 점을 빠르게 확인하세요." />
      <Section className="max-w-3xl">
        {Object.keys(grouped).length === 0 && (
          <p className="text-center text-slate-400">등록된 FAQ가 없습니다.</p>
        )}
        {Object.entries(grouped).map(([cat, items]) => (
          <div key={cat} className="mb-8">
            <h2 className="mb-3 text-lg font-extrabold text-slate-900">{cat}</h2>
            <div className="space-y-3">
              {items.map((f) => (
                <details
                  key={f.id}
                  className="group rounded-2xl border border-slate-200 bg-white p-5 open:border-brand-200 open:shadow-sm"
                >
                  <summary className="flex cursor-pointer list-none items-center gap-3 font-bold text-slate-800">
                    <span className="grid h-6 w-6 place-items-center rounded-full bg-brand-50 text-sm text-brand-600">Q</span>
                    <span className="flex-1">{f.question}</span>
                    <span className="text-slate-400 transition group-open:rotate-180">⌄</span>
                  </summary>
                  <p className="mt-3 whitespace-pre-wrap pl-9 leading-7 text-slate-600">{f.answer}</p>
                </details>
              ))}
            </div>
          </div>
        ))}
      </Section>
    </>
  );
}
