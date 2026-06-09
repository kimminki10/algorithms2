import Link from "next/link";
import { prisma } from "@/lib/prisma";
import { deleteNotice } from "../actions";

export const metadata = { title: "공지 관리" };

export default async function AdminNotices() {
  const notices = await prisma.notice.findMany({
    orderBy: [{ pinned: "desc" }, { createdAt: "desc" }],
  });

  return (
    <div>
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-900">공지 관리</h1>
          <p className="mt-1 text-slate-500">공지사항을 작성·수정·삭제합니다.</p>
        </div>
        <Link href="/admin/notices/new" className="rounded-xl bg-brand-500 px-5 py-2.5 text-sm font-bold text-white hover:bg-brand-600">
          + 새 공지
        </Link>
      </div>

      <div className="mt-5 overflow-hidden rounded-2xl border border-slate-200 bg-white">
        <ul className="divide-y divide-slate-100">
          {notices.length === 0 && <li className="px-5 py-10 text-center text-slate-400">등록된 공지가 없습니다.</li>}
          {notices.map((n) => (
            <li key={n.id} className="flex items-center gap-3 px-5 py-4">
              {n.pinned && <span className="rounded bg-rose-100 px-2 py-0.5 text-xs font-bold text-rose-600">중요</span>}
              <Link href={`/admin/notices/${n.id}`} className="flex-1 truncate font-semibold text-slate-800 hover:text-brand-600">
                {n.title}
              </Link>
              <span className="hidden text-sm text-slate-400 sm:inline">{new Date(n.createdAt).toLocaleDateString("ko-KR")}</span>
              <Link href={`/admin/notices/${n.id}`} className="rounded-lg border border-slate-300 px-3 py-1.5 text-xs font-semibold text-slate-600 hover:bg-slate-50">
                수정
              </Link>
              <form action={deleteNotice}>
                <input type="hidden" name="id" value={n.id} />
                <button className="rounded-lg border border-rose-200 px-3 py-1.5 text-xs font-semibold text-rose-600 hover:bg-rose-50">
                  삭제
                </button>
              </form>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
