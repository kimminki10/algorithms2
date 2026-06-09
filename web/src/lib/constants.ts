export const SITE = {
  name: "한빛 종합지원센터",
  short: "한빛센터",
  tagline: "지역과 함께 성장하는 열린 공간",
  tel: "054-000-0000",
  email: "contact@hanbit.example.kr",
  address: "경상북도 ○○시 ○○로 123",
};

export const APP_TYPES = {
  RENTAL: { label: "대관 신청", desc: "회의실·강당 등 시설 대관", icon: "🏛️" },
  PROGRAM: { label: "프로그램 신청", desc: "교육·강좌 등 프로그램 참여", icon: "📚" },
  BUSINESS: { label: "사업 신청", desc: "지원사업·공모 신청 접수", icon: "💼" },
} as const;

export type AppType = keyof typeof APP_TYPES;

export const APP_STATUS = {
  PENDING: { label: "접수", color: "bg-amber-100 text-amber-700" },
  APPROVED: { label: "승인", color: "bg-emerald-100 text-emerald-700" },
  REJECTED: { label: "반려", color: "bg-rose-100 text-rose-700" },
} as const;

export type AppStatus = keyof typeof APP_STATUS;

// 대관 가능 시설 (데모용 고정 목록 — 운영 시 DB/관리자 관리로 확장 가능)
export const FACILITIES = [
  { id: "hall", name: "대강당", capacity: 200, desc: "행사·공연용 대규모 공간" },
  { id: "seminar", name: "세미나실", capacity: 40, desc: "강의·발표에 적합" },
  { id: "meeting", name: "소회의실", capacity: 12, desc: "소규모 회의·모임" },
  { id: "multi", name: "다목적홀", capacity: 80, desc: "교육·워크숍 등 다용도" },
] as const;

export type FacilityId = (typeof FACILITIES)[number]["id"];

export function facilityName(id?: string | null) {
  return FACILITIES.find((f) => f.id === id)?.name ?? id ?? "-";
}

// 대관 시간대
export const TIME_SLOTS = [
  { id: "AM", label: "오전", time: "09:00 ~ 12:00" },
  { id: "PM", label: "오후", time: "13:00 ~ 17:00" },
  { id: "EV", label: "저녁", time: "18:00 ~ 21:00" },
] as const;

export type SlotId = (typeof TIME_SLOTS)[number]["id"];

export function slotLabel(id?: string | null) {
  const s = TIME_SLOTS.find((s) => s.id === id);
  return s ? `${s.label} (${s.time})` : id ?? "-";
}

// 예약을 점유로 간주하는 상태 (중복 방지 기준)
export const ACTIVE_BOOKING_STATUS = ["PENDING", "APPROVED"];

