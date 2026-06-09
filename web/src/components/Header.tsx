import Link from "next/link";
import { getSession, destroySession } from "@/lib/auth";
import { redirect } from "next/navigation";
import { SITE } from "@/lib/constants";

const nav = [
  { href: "/about", label: "기관소개" },
  { href: "/notices", label: "공지사항" },
  { href: "/apply", label: "신청" },
  { href: "/faq", label: "FAQ" },
];

async function logout() {
  "use server";
  await destroySession();
  redirect("/");
}

export default async function Header() {
  const user = await getSession();
  return (
    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-6xl items-center gap-6 px-5">
        <Link href="/" className="flex items-center gap-2 font-extrabold text-slate-900">
          <span className="grid h-9 w-9 place-items-center rounded-xl bg-brand-500 text-white">한</span>
          <span className="text-lg tracking-tight">{SITE.name}</span>
        </Link>

        <nav className="hidden items-center gap-1 md:flex">
          {nav.map((n) => (
            <Link
              key={n.href}
              href={n.href}
              className="rounded-lg px-3 py-2 text-sm font-semibold text-slate-600 transition hover:bg-slate-100 hover:text-slate-900"
            >
              {n.label}
            </Link>
          ))}
        </nav>

        <div className="ml-auto flex items-center gap-2 text-sm">
          {user ? (
            <>
              {user.role === "ADMIN" && (
                <Link href="/admin" className="rounded-lg px-3 py-2 font-semibold text-brand-600 hover:bg-brand-50">
                  관리자
                </Link>
              )}
              <span className="hidden text-slate-500 sm:inline">{user.name}님</span>
              <form action={logout}>
                <button className="rounded-lg border border-slate-300 px-3 py-2 font-semibold text-slate-700 hover:bg-slate-50">
                  로그아웃
                </button>
              </form>
            </>
          ) : (
            <>
              <Link href="/login" className="rounded-lg px-3 py-2 font-semibold text-slate-700 hover:bg-slate-100">
                로그인
              </Link>
              <Link href="/signup" className="rounded-lg bg-brand-500 px-4 py-2 font-semibold text-white hover:bg-brand-600">
                회원가입
              </Link>
            </>
          )}
        </div>
      </div>

      {/* mobile nav */}
      <nav className="flex items-center gap-1 overflow-x-auto border-t border-slate-100 px-3 py-2 md:hidden">
        {nav.map((n) => (
          <Link
            key={n.href}
            href={n.href}
            className="whitespace-nowrap rounded-lg px-3 py-1.5 text-sm font-semibold text-slate-600 hover:bg-slate-100"
          >
            {n.label}
          </Link>
        ))}
      </nav>
    </header>
  );
}
