import { prisma } from "@/lib/prisma";
import { APP_TYPES, APP_STATUS, facilityName, slotLabel, type AppType, type AppStatus } from "@/lib/constants";
import { updateApplicationStatus } from "../actions";

export const metadata = { title: "신청 관리" };

export default async function AdminApplications({
  searchParams,
}: {
  searchParams: Promise<{ status?: string }>;
}) {
  const { status } = await searchParams;
  const where = status && status in APP_STATUS ? { status } : {};
  const apps = await prisma.application.findMany({ where, orderBy: { createdAt: "desc" } });

  const filters = [{ key: "", label: "전체" }, ...Object.entries(APP_STATUS).map(([k, v]) => ({ key: k, label: v.label }))];

  return (
    <div>
      <h1 className="text-2xl font-extrabold text-slate-900">신청 관리</h1>
      <p className="mt-1 text-slate-500">접수된 신청을 검토하고 승인/반려 처리하세요.</p>

      <div className="mt-5 flex gap-2">
        {filters.map((f) => (
          <a
            key={f.key}
            href={`/admin/applications${f.key ? `?status=${f.key}` : ""}`}
            className={`rounded-full px-4 py-1.5 text-sm font-semibold ${
              (status ?? "") === f.key ? "bg-brand-500 text-white" : "bg-white text-slate-600 border border-slate-200"
            }`}
          >
            {f.label}
          </a>
        ))}
      </div>

      <div className="mt-5 space-y-4">
        {apps.length === 0 && (
          <p className="rounded-2xl border border-slate-200 bg-white px-6 py-10 text-center text-slate-400">신청 내역이 없습니다.</p>
        )}
        {apps.map((a) => (
          <div key={a.id} className="rounded-2xl border border-slate-200 bg-white p-5">
            <div className="flex flex-wrap items-center gap-2">
              <span className="rounded-full bg-slate-100 px-2.5 py-0.5 text-xs font-bold text-slate-600">
                {APP_TYPES[a.type as AppType].label}
              </span>
              <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${APP_STATUS[a.status as AppStatus].color}`}>
                {APP_STATUS[a.status as AppStatus].label}
              </span>
              <span className="ml-auto text-sm text-slate-400">{new Date(a.createdAt).toLocaleString("ko-KR")}</span>
            </div>

            <h3 className="mt-3 font-bold text-slate-900">{a.title}</h3>
            {a.type === "RENTAL" && (
              <p className="mt-1 inline-block rounded-lg bg-brand-50 px-3 py-1 text-sm font-semibold text-brand-700">
                🏛️ {facilityName(a.facility)} · {a.desiredDate} · {slotLabel(a.timeSlot)}
              </p>
            )}
            <p className="mt-2 whitespace-pre-wrap text-sm text-slate-600">{a.content}</p>

            <dl className="mt-3 grid gap-x-6 gap-y-1 text-sm text-slate-500 sm:grid-cols-2">
              <div><dt className="inline font-semibold">신청자: </dt><dd className="inline">{a.applicantName}</dd></div>
              <div><dt className="inline font-semibold">연락처: </dt><dd className="inline">{a.phone}</dd></div>
              <div><dt className="inline font-semibold">이메일: </dt><dd className="inline">{a.email}</dd></div>
            </dl>

            <form action={updateApplicationStatus} className="mt-4 flex flex-col gap-2 border-t border-slate-100 pt-4 sm:flex-row sm:items-center">
              <input type="hidden" name="id" value={a.id} />
              <select name="status" defaultValue={a.status} className="rounded-lg border border-slate-300 px-3 py-2 text-sm">
                {Object.entries(APP_STATUS).map(([k, v]) => (
                  <option key={k} value={k}>{v.label}</option>
                ))}
              </select>
              <input
                name="adminNote"
                defaultValue={a.adminNote ?? ""}
                placeholder="신청자에게 전달할 메모 (선택)"
                className="flex-1 rounded-lg border border-slate-300 px-3 py-2 text-sm"
              />
              <button className="rounded-lg bg-brand-500 px-4 py-2 text-sm font-bold text-white hover:bg-brand-600">저장</button>
            </form>
          </div>
        ))}
      </div>
    </div>
  );
}
