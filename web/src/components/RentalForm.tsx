"use client";

import { useMemo, useState } from "react";
import { FACILITIES, TIME_SLOTS } from "@/lib/constants";
import { submitApplication } from "@/app/(site)/apply/actions";

type Booking = { facility: string | null; desiredDate: string | null; timeSlot: string | null };

const WD = ["일", "월", "화", "수", "목", "금", "토"];
const ymd = (y: number, m: number, d: number) =>
  `${y}-${String(m + 1).padStart(2, "0")}-${String(d).padStart(2, "0")}`;

export default function RentalForm({
  bookings,
  defaultName,
  defaultEmail,
}: {
  bookings: Booking[];
  defaultName?: string;
  defaultEmail?: string;
}) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const [facility, setFacility] = useState<string>(FACILITIES[0].id);
  const [view, setView] = useState({ y: today.getFullYear(), m: today.getMonth() });
  const [date, setDate] = useState<string>("");
  const [slot, setSlot] = useState<string>("");

  // 선택 시설의 점유 슬롯 집합: "YYYY-MM-DD|SLOT"
  const booked = useMemo(() => {
    const set = new Set<string>();
    for (const b of bookings) {
      if (b.facility === facility && b.desiredDate && b.timeSlot) {
        set.add(`${b.desiredDate}|${b.timeSlot}`);
      }
    }
    return set;
  }, [bookings, facility]);

  const availableSlots = (d: string) => TIME_SLOTS.filter((s) => !booked.has(`${d}|${s.id}`));

  const grid = useMemo(() => {
    const first = new Date(view.y, view.m, 1);
    const startPad = first.getDay();
    const days = new Date(view.y, view.m + 1, 0).getDate();
    const cells: ({ d: string; day: number; past: boolean; avail: number } | null)[] = [];
    for (let i = 0; i < startPad; i++) cells.push(null);
    for (let day = 1; day <= days; day++) {
      const d = ymd(view.y, view.m, day);
      const cur = new Date(view.y, view.m, day);
      cells.push({ d, day, past: cur < today, avail: availableSlots(d).length });
    }
    return cells;
  }, [view, booked]); // eslint-disable-line react-hooks/exhaustive-deps

  const canPrev = view.y > today.getFullYear() || (view.y === today.getFullYear() && view.m > today.getMonth());
  const shift = (dir: number) => {
    setDate(""); setSlot("");
    setView((v) => {
      const nm = v.m + dir;
      return { y: v.y + Math.floor(nm / 12), m: ((nm % 12) + 12) % 12 };
    });
  };

  const inputCls =
    "mt-1.5 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-100";

  const slotsForDate = date ? TIME_SLOTS.map((s) => ({ ...s, taken: booked.has(`${date}|${s.id}`) })) : [];

  return (
    <form action={submitApplication} className="space-y-6">
      <input type="hidden" name="type" value="RENTAL" />
      <input type="hidden" name="facility" value={facility} />
      <input type="hidden" name="desiredDate" value={date} />
      <input type="hidden" name="timeSlot" value={slot} />

      {/* 1. 시설 선택 */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="flex items-center gap-2 font-bold text-slate-900">
          <span className="grid h-6 w-6 place-items-center rounded-full bg-brand-500 text-xs text-white">1</span>
          시설 선택
        </h2>
        <div className="mt-4 grid gap-3 sm:grid-cols-2">
          {FACILITIES.map((f) => (
            <button
              type="button"
              key={f.id}
              onClick={() => { setFacility(f.id); setDate(""); setSlot(""); }}
              className={`rounded-xl border p-4 text-left transition ${
                facility === f.id ? "border-brand-500 bg-brand-50 ring-2 ring-brand-100" : "border-slate-200 hover:border-brand-200"
              }`}
            >
              <div className="font-bold text-slate-900">{f.name}</div>
              <div className="mt-0.5 text-xs text-slate-500">{f.desc} · 정원 {f.capacity}명</div>
            </button>
          ))}
        </div>
      </div>

      {/* 2. 날짜 선택 (달력) */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="flex items-center gap-2 font-bold text-slate-900">
          <span className="grid h-6 w-6 place-items-center rounded-full bg-brand-500 text-xs text-white">2</span>
          날짜 선택
        </h2>

        <div className="mt-4 flex items-center justify-between">
          <button type="button" disabled={!canPrev} onClick={() => shift(-1)} className="rounded-lg px-3 py-1.5 text-sm font-bold text-slate-600 enabled:hover:bg-slate-100 disabled:opacity-30">‹ 이전</button>
          <span className="font-bold text-slate-900">{view.y}년 {view.m + 1}월</span>
          <button type="button" onClick={() => shift(1)} className="rounded-lg px-3 py-1.5 text-sm font-bold text-slate-600 hover:bg-slate-100">다음 ›</button>
        </div>

        <div className="mt-3 grid grid-cols-7 gap-1 text-center text-xs font-bold text-slate-400">
          {WD.map((w, i) => <div key={w} className={`py-1 ${i === 0 ? "text-rose-400" : i === 6 ? "text-brand-400" : ""}`}>{w}</div>)}
        </div>
        <div className="mt-1 grid grid-cols-7 gap-1">
          {grid.map((c, i) => {
            if (!c) return <div key={i} />;
            const disabled = c.past || c.avail === 0;
            const selected = date === c.d;
            return (
              <button
                type="button"
                key={c.d}
                disabled={disabled}
                onClick={() => { setDate(c.d); setSlot(""); }}
                className={`flex h-12 flex-col items-center justify-center rounded-lg text-sm transition ${
                  selected ? "bg-brand-500 text-white font-bold"
                  : disabled ? "cursor-not-allowed text-slate-300"
                  : "hover:bg-brand-50 text-slate-700"
                }`}
              >
                <span>{c.day}</span>
                {!c.past && (
                  <span className={`text-[10px] ${c.avail === 0 ? "text-rose-400" : selected ? "text-brand-100" : "text-emerald-500"}`}>
                    {c.avail === 0 ? "마감" : `${c.avail}자리`}
                  </span>
                )}
              </button>
            );
          })}
        </div>
        <p className="mt-3 text-xs text-slate-400">초록 숫자는 예약 가능한 시간대 수입니다. ‘마감’은 모든 시간대가 예약된 날짜입니다.</p>
      </div>

      {/* 3. 시간대 선택 */}
      <div className={`rounded-2xl border border-slate-200 bg-white p-6 ${!date ? "opacity-50" : ""}`}>
        <h2 className="flex items-center gap-2 font-bold text-slate-900">
          <span className="grid h-6 w-6 place-items-center rounded-full bg-brand-500 text-xs text-white">3</span>
          시간대 선택 {date && <span className="text-sm font-normal text-slate-400">— {date}</span>}
        </h2>
        {!date ? (
          <p className="mt-4 text-sm text-slate-400">먼저 날짜를 선택하세요.</p>
        ) : (
          <div className="mt-4 grid gap-3 sm:grid-cols-3">
            {slotsForDate.map((s) => (
              <button
                type="button"
                key={s.id}
                disabled={s.taken}
                onClick={() => setSlot(s.id)}
                className={`rounded-xl border p-4 text-center transition ${
                  s.taken ? "cursor-not-allowed border-slate-100 bg-slate-50 text-slate-300"
                  : slot === s.id ? "border-brand-500 bg-brand-50 ring-2 ring-brand-100"
                  : "border-slate-200 hover:border-brand-200"
                }`}
              >
                <div className="font-bold text-slate-900">{s.label}</div>
                <div className="mt-0.5 text-xs text-slate-500">{s.time}</div>
                {s.taken && <div className="mt-1 text-xs font-bold text-rose-400">예약 마감</div>}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* 4. 신청자 정보 */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="flex items-center gap-2 font-bold text-slate-900">
          <span className="grid h-6 w-6 place-items-center rounded-full bg-brand-500 text-xs text-white">4</span>
          신청 정보
        </h2>
        <div className="mt-4 space-y-4">
          <label className="block">
            <span className="text-sm font-semibold text-slate-700">사용 목적(제목) <span className="text-rose-500">*</span></span>
            <input name="title" required className={inputCls} placeholder="예: 동아리 정기모임" />
          </label>
          <div className="grid gap-4 sm:grid-cols-2">
            <label className="block">
              <span className="text-sm font-semibold text-slate-700">신청자명 <span className="text-rose-500">*</span></span>
              <input name="applicantName" required defaultValue={defaultName} className={inputCls} />
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-slate-700">연락처 <span className="text-rose-500">*</span></span>
              <input name="phone" required placeholder="010-0000-0000" className={inputCls} />
            </label>
          </div>
          <label className="block">
            <span className="text-sm font-semibold text-slate-700">이메일 <span className="text-rose-500">*</span></span>
            <input name="email" type="email" required defaultValue={defaultEmail} className={inputCls} />
          </label>
          <label className="block">
            <span className="text-sm font-semibold text-slate-700">상세 내용 <span className="text-rose-500">*</span></span>
            <textarea name="content" required rows={4} className={inputCls} placeholder="이용 인원, 준비물, 요청사항 등을 적어주세요." />
          </label>
        </div>
      </div>

      {/* 요약 + 제출 */}
      <div className="flex flex-col gap-3 rounded-2xl border border-brand-200 bg-brand-50 p-5 sm:flex-row sm:items-center">
        <div className="flex-1 text-sm">
          <span className="font-bold text-slate-900">{FACILITIES.find((f) => f.id === facility)?.name}</span>
          <span className="text-slate-500">
            {date ? ` · ${date}` : " · 날짜 미선택"}
            {slot ? ` · ${TIME_SLOTS.find((s) => s.id === slot)?.label}` : ""}
          </span>
        </div>
        <button
          type="submit"
          disabled={!date || !slot}
          className="rounded-xl bg-brand-500 px-6 py-2.5 text-sm font-bold text-white transition hover:bg-brand-600 disabled:cursor-not-allowed disabled:opacity-50"
        >
          대관 신청하기
        </button>
      </div>
    </form>
  );
}
