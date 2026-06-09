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
