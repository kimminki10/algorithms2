import type { Metadata } from "next";
import "./globals.css";
import { SITE } from "@/lib/constants";

export const metadata: Metadata = {
  title: {
    default: `${SITE.name}`,
    template: `%s | ${SITE.name}`,
  },
  description: `${SITE.name} — ${SITE.tagline}. 기관 소개, 공지사항, 대관·프로그램·사업 신청, FAQ를 한 곳에서.`,
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko" className="h-full antialiased">
      <head>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css"
        />
      </head>
      <body className="min-h-full bg-slate-50 text-slate-800">{children}</body>
    </html>
  );
}
