import Link from "next/link";
import { redirect } from "next/navigation";
import { getSession, destroySession } from "@/lib/auth";
import { SITE } from "@/lib/constants";

const menu = [
  { href: "/admin", label: "대시보드", icon: "📊" },
  { href: "/admin/applications", label: "신청 관리", icon: "📝" },
  { href: "/admin/notices", label: "공지 관리", icon: "📢" },
  { href: "/admin/faq", label: "FAQ 관리", icon: "❓" },
];

async function logout() {
  "use server";
  await destroySession();
  redirect("/login");
}

export default async function AdminLayout({ children }: { children: React.ReactNode }) {
  const user = await getSession();
  if (!user) redirect("/login?next=/admin");
  if (user.role !== "ADMIN") redirect("/");

  return (
    <div className="flex min-h-screen bg-slate-100">
      <aside className="hidden w-60 flex-col border-r border-slate-200 bg-white p-4 md:flex">
        <Link href="/" className="flex items-center gap-2 px-2 py-3 font-extrabold text-slate-900">
          <span className="grid h-8 w-8 place-items-center rounded-lg bg-brand-500 text-white">한</span>
          <span className="text-sm">{SITE.short} 관리자</span>
        </Link>
        <nav className="mt-4 space-y-1">
          {menu.map((m) => (
            <Link
              key={m.href}
              href={m.href}
              className="flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-semibold text-slate-600 hover:bg-slate-100 hover:text-slate-900"
            >
              <span>{m.icon}</span> {m.label}
            </Link>
          ))}
        </nav>
        <form action={logout} className="mt-auto">
          <button className="w-full rounded-xl border border-slate-300 py-2 text-sm font-semibold text-slate-600 hover:bg-slate-50">
            로그아웃
          </button>
        </form>
      </aside>

      <div className="flex-1">
        <header className="flex items-center gap-3 border-b border-slate-200 bg-white px-5 py-3 md:hidden">
          <span className="font-extrabold">{SITE.short} 관리자</span>
          <nav className="ml-auto flex gap-1 overflow-x-auto text-sm">
            {menu.map((m) => (
              <Link key={m.href} href={m.href} className="whitespace-nowrap rounded-lg px-2 py-1 font-semibold text-slate-600 hover:bg-slate-100">
                {m.icon}
              </Link>
            ))}
          </nav>
        </header>
        <main className="mx-auto max-w-5xl p-5 md:p-8">{children}</main>
      </div>
    </div>
  );
}
