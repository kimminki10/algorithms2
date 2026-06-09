import Link from "next/link";
import { SITE } from "@/lib/constants";

export default function Footer() {
  return (
    <footer className="mt-20 border-t border-slate-200 bg-white">
      <div className="mx-auto grid max-w-6xl gap-8 px-5 py-12 md:grid-cols-3">
        <div>
          <div className="flex items-center gap-2 font-extrabold text-slate-900">
            <span className="grid h-8 w-8 place-items-center rounded-lg bg-brand-500 text-white">한</span>
            {SITE.name}
          </div>
          <p className="mt-3 text-sm text-slate-500">{SITE.tagline}</p>
        </div>
        <div className="text-sm text-slate-600">
          <p className="font-semibold text-slate-800">바로가기</p>
          <ul className="mt-3 space-y-1.5">
            <li><Link href="/about" className="hover:text-brand-600">기관소개</Link></li>
            <li><Link href="/notices" className="hover:text-brand-600">공지사항</Link></li>
            <li><Link href="/apply" className="hover:text-brand-600">신청</Link></li>
            <li><Link href="/faq" className="hover:text-brand-600">FAQ</Link></li>
          </ul>
        </div>
        <div className="text-sm text-slate-600">
          <p className="font-semibold text-slate-800">문의</p>
          <ul className="mt-3 space-y-1.5">
            <li>전화 · {SITE.tel}</li>
            <li>이메일 · {SITE.email}</li>
            <li>{SITE.address}</li>
          </ul>
        </div>
      </div>
      <div className="border-t border-slate-100 py-5 text-center text-xs text-slate-400">
        © {new Date().getFullYear()} {SITE.name}. All rights reserved.
      </div>
    </footer>
  );
}
