import { redirect } from "next/navigation";
import { prisma } from "@/lib/prisma";
import { getSession } from "@/lib/auth";
import { PageHero, Section, Badge } from "@/components/ui";
import { APP_TYPES, APP_STATUS, facilityName, slotLabel, type AppType, type AppStatus } from "@/lib/constants";

export const metadata = { title: "마이페이지" };

export default async function MyPage() {
  const user = await getSession();
  if (!user) redirect("/login?next=/mypage");

  const apps = await prisma.application.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
  });

  return (
    <>
      <PageHero crumb="MYPAGE" title="마이페이지" subtitle={`${user.name}님의 신청 현황입니다.`} />
      <Section>
        <h2 className="text-lg font-extrabold text-slate-900">나의 신청 내역</h2>
        <div className="mt-4 space-y-3">
          {apps.length === 0 && (
            <p className="rounded-2xl border border-slate-200 bg-white px-6 py-10 text-center text-slate-400">
              신청 내역이 없습니다.
            </p>
          )}
          {apps.map((a) => (
            <div key={a.id} className="rounded-2xl border border-slate-200 bg-white p-5">
              <div className="flex items-center gap-3">
                <Badge className="bg-slate-100 text-slate-600">{APP_TYPES[a.type as AppType].label}</Badge>
                <Badge className={APP_STATUS[a.status as AppStatus].color}>{APP_STATUS[a.status as AppStatus].label}</Badge>
                <span className="ml-auto text-sm text-slate-400">{new Date(a.createdAt).toLocaleDateString("ko-KR")}</span>
              </div>
              <h3 className="mt-3 font-bold text-slate-900">{a.title}</h3>
              {a.type === "RENTAL" && (
                <p className="mt-1 text-sm font-semibold text-brand-600">
                  {facilityName(a.facility)} · {a.desiredDate} · {slotLabel(a.timeSlot)}
                </p>
              )}
              <p className="mt-1 line-clamp-2 text-sm text-slate-500">{a.content}</p>
              {a.adminNote && (
                <p className="mt-3 rounded-lg bg-slate-50 px-3 py-2 text-sm text-slate-600">
                  <b>담당자 메모:</b> {a.adminNote}
                </p>
              )}
            </div>
          ))}
        </div>
      </Section>
    </>
  );
}
