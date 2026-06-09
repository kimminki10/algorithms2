import Link from "next/link";
import { prisma } from "@/lib/prisma";
import { APP_TYPES, APP_STATUS, type AppType, type AppStatus } from "@/lib/constants";

export const metadata = { title: "관리자 대시보드" };

export default async function AdminDashboard() {
  const [pending, total, notices, members, recent] = await Promise.all([
    prisma.application.count({ where: { status: "PENDING" } }),
    prisma.application.count(),
    prisma.notice.count(),
    prisma.user.count(),
    prisma.application.findMany({ orderBy: { createdAt: "desc" }, take: 5 }),
  ]);

  const stats = [
    { label: "대기 중인 신청", value: pending, href: "/admin/applications", accent: "text-amber-600" },
    { label: "전체 신청", value: total, href: "/admin/applications", accent: "text-brand-600" },
    { label: "공지사항", value: notices, href: "/admin/notices", accent: "text-slate-900" },
    { label: "회원 수", value: members, href: "/admin", accent: "text-slate-900" },
  ];

  return (
    <div>
      <h1 className="text-2xl font-extrabold text-slate-900">대시보드</h1>
      <p className="mt-1 text-slate-500">센터 운영 현황을 한눈에 확인하세요.</p>

      <div className="mt-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {stats.map((s) => (
          <Link key={s.label} href={s.href} className="rounded-2xl border border-slate-200 bg-white p-5 hover:shadow-sm">
            <div className={`text-3xl font-extrabold ${s.accent}`}>{s.value}</div>
            <div className="mt-1 text-sm text-slate-500">{s.label}</div>
          </Link>
        ))}
      </div>

      <h2 className="mt-10 text-lg font-extrabold text-slate-900">최근 신청</h2>
      <div className="mt-3 overflow-hidden rounded-2xl border border-slate-200 bg-white">
        <ul className="divide-y divide-slate-100">
          {recent.length === 0 && <li className="px-5 py-8 text-center text-slate-400">신청 내역이 없습니다.</li>}
          {recent.map((a) => (
            <li key={a.id} className="flex items-center gap-3 px-5 py-3 text-sm">
              <span className="rounded-full bg-slate-100 px-2 py-0.5 text-xs font-bold text-slate-600">
                {APP_TYPES[a.type as AppType].label}
              </span>
              <span className="flex-1 truncate font-semibold text-slate-800">{a.title}</span>
              <span className={`rounded-full px-2 py-0.5 text-xs font-bold ${APP_STATUS[a.status as AppStatus].color}`}>
                {APP_STATUS[a.status as AppStatus].label}
              </span>
              <span className="hidden text-slate-400 sm:inline">{new Date(a.createdAt).toLocaleDateString("ko-KR")}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
