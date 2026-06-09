import Link from "next/link";
import { prisma } from "@/lib/prisma";
import { PageHero, Section } from "@/components/ui";

export const metadata = { title: "공지사항" };

export default async function NoticesPage() {
  const notices = await prisma.notice.findMany({
    orderBy: [{ pinned: "desc" }, { createdAt: "desc" }],
  });

  return (
    <>
      <PageHero crumb="NOTICE" title="공지사항" subtitle="센터의 소식과 안내사항을 확인하세요." />
      <Section>
        <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white">
          <div className="hidden grid-cols-[60px_1fr_120px_80px] gap-4 border-b border-slate-200 bg-slate-50 px-6 py-3 text-xs font-bold text-slate-500 md:grid">
            <span>번호</span><span>제목</span><span>등록일</span><span className="text-right">조회</span>
          </div>
          <ul className="divide-y divide-slate-100">
            {notices.length === 0 && (
              <li className="px-6 py-10 text-center text-slate-400">등록된 공지가 없습니다.</li>
            )}
            {notices.map((n, i) => (
              <li key={n.id}>
                <Link
                  href={`/notices/${n.id}`}
                  className="grid grid-cols-1 gap-1 px-6 py-4 hover:bg-slate-50 md:grid-cols-[60px_1fr_120px_80px] md:items-center md:gap-4"
                >
                  <span className="text-sm text-slate-400">
                    {n.pinned ? <span className="rounded bg-rose-100 px-2 py-0.5 text-xs font-bold text-rose-600">중요</span> : notices.length - i}
                  </span>
                  <span className="font-semibold text-slate-800">{n.title}</span>
                  <span className="text-sm text-slate-400">{new Date(n.createdAt).toLocaleDateString("ko-KR")}</span>
                  <span className="text-sm text-slate-400 md:text-right">{n.views}</span>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </Section>
    </>
  );
}
