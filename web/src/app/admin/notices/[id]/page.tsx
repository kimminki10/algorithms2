import Link from "next/link";
import { notFound } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { createNotice, updateNotice } from "../../actions";

export default async function NoticeEditor({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const isNew = id === "new";

  const notice = isNew ? null : await prisma.notice.findUnique({ where: { id } });
  if (!isNew && !notice) notFound();

  const inputCls =
    "mt-1.5 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-100";

  return (
    <div>
      <Link href="/admin/notices" className="text-sm font-bold text-brand-600 hover:underline">← 공지 목록</Link>
      <h1 className="mt-2 text-2xl font-extrabold text-slate-900">{isNew ? "새 공지 작성" : "공지 수정"}</h1>

      <form action={isNew ? createNotice : updateNotice} className="mt-5 space-y-5 rounded-2xl border border-slate-200 bg-white p-6">
        {!isNew && <input type="hidden" name="id" value={notice!.id} />}

        <label className="block">
          <span className="text-sm font-semibold text-slate-700">제목</span>
          <input name="title" required defaultValue={notice?.title} className={inputCls} placeholder="공지 제목" />
        </label>

        <label className="block">
          <span className="text-sm font-semibold text-slate-700">내용</span>
          <textarea name="content" required rows={12} defaultValue={notice?.content} className={inputCls} placeholder="공지 내용을 입력하세요." />
        </label>

        <label className="flex items-center gap-2">
          <input type="checkbox" name="pinned" defaultChecked={notice?.pinned} className="h-4 w-4 rounded border-slate-300" />
          <span className="text-sm font-semibold text-slate-700">상단 고정 (중요 공지)</span>
        </label>

        <div className="flex justify-end gap-2 pt-2">
          <Link href="/admin/notices" className="rounded-xl border border-slate-300 px-5 py-2.5 text-sm font-bold text-slate-700 hover:bg-slate-50">
            취소
          </Link>
          <button className="rounded-xl bg-brand-500 px-5 py-2.5 text-sm font-bold text-white hover:bg-brand-600">
            {isNew ? "등록" : "저장"}
          </button>
        </div>
      </form>
    </div>
  );
}
