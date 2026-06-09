import { prisma } from "@/lib/prisma";
import { createFaq, deleteFaq } from "../actions";

export const metadata = { title: "FAQ 관리" };

export default async function AdminFaq() {
  const faqs = await prisma.faq.findMany({ orderBy: [{ category: "asc" }, { sort: "asc" }] });

  const inputCls =
    "mt-1.5 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-100";

  return (
    <div>
      <h1 className="text-2xl font-extrabold text-slate-900">FAQ 관리</h1>
      <p className="mt-1 text-slate-500">자주 묻는 질문을 등록하고 관리합니다.</p>

      <form action={createFaq} className="mt-5 space-y-4 rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="font-bold text-slate-900">새 FAQ 등록</h2>
        <div className="grid gap-4 sm:grid-cols-[160px_1fr]">
          <label className="block">
            <span className="text-sm font-semibold text-slate-700">분류</span>
            <input name="category" defaultValue="일반" className={inputCls} />
          </label>
          <label className="block">
            <span className="text-sm font-semibold text-slate-700">질문</span>
            <input name="question" required className={inputCls} placeholder="질문을 입력하세요" />
          </label>
        </div>
        <label className="block">
          <span className="text-sm font-semibold text-slate-700">답변</span>
          <textarea name="answer" required rows={4} className={inputCls} placeholder="답변을 입력하세요" />
        </label>
        <div className="flex justify-end">
          <button className="rounded-xl bg-brand-500 px-5 py-2.5 text-sm font-bold text-white hover:bg-brand-600">등록</button>
        </div>
      </form>

      <div className="mt-6 space-y-3">
        {faqs.map((f) => (
          <div key={f.id} className="rounded-2xl border border-slate-200 bg-white p-5">
            <div className="flex items-start gap-3">
              <span className="rounded-full bg-slate-100 px-2.5 py-0.5 text-xs font-bold text-slate-600">{f.category}</span>
              <div className="flex-1">
                <p className="font-bold text-slate-900">Q. {f.question}</p>
                <p className="mt-1 whitespace-pre-wrap text-sm text-slate-600">A. {f.answer}</p>
              </div>
              <form action={deleteFaq}>
                <input type="hidden" name="id" value={f.id} />
                <button className="rounded-lg border border-rose-200 px-3 py-1.5 text-xs font-semibold text-rose-600 hover:bg-rose-50">삭제</button>
              </form>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
