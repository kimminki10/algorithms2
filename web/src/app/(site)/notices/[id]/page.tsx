import Link from "next/link";
import { notFound } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { Section, Button } from "@/components/ui";

export default async function NoticeDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  const notice = await prisma.notice.update({
    where: { id },
    data: { views: { increment: 1 } },
  }).catch(() => null);

  if (!notice) notFound();

  return (
    <Section className="max-w-3xl">
      <p className="text-sm font-bold text-brand-600">공지사항</p>
      <h1 className="mt-2 text-2xl font-extrabold text-slate-900">{notice.title}</h1>
      <div className="mt-3 flex gap-4 border-b border-slate-200 pb-4 text-sm text-slate-400">
        <span>{new Date(notice.createdAt).toLocaleDateString("ko-KR")}</span>
        <span>조회 {notice.views}</span>
      </div>
      <article className="mt-6 min-h-40 whitespace-pre-wrap leading-8 text-slate-700">
        {notice.content}
      </article>
      <div className="mt-10">
        <Button href="/notices" variant="outline">← 목록으로</Button>
      </div>
    </Section>
  );
}
