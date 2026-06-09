"use client";

import Link from "next/link";
import { useActionState } from "react";
import { login, signup } from "@/app/login/actions";
import { SITE } from "@/lib/constants";

type Mode = "login" | "signup";

export default function AuthForm({ mode, next = "/" }: { mode: Mode; next?: string }) {
  const action = mode === "login" ? login : signup;
  const [state, formAction, pending] = useActionState(action, null as { error?: string } | null);

  const cls =
    "mt-1.5 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-100";

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-50 px-5 py-12">
      <div className="w-full max-w-md">
        <Link href="/" className="flex items-center justify-center gap-2 font-extrabold text-slate-900">
          <span className="grid h-10 w-10 place-items-center rounded-xl bg-brand-500 text-white">한</span>
          <span className="text-lg">{SITE.name}</span>
        </Link>

        <div className="mt-6 rounded-2xl border border-slate-200 bg-white p-8 shadow-sm">
          <h1 className="text-xl font-extrabold text-slate-900">
            {mode === "login" ? "로그인" : "회원가입"}
          </h1>
          <p className="mt-1 text-sm text-slate-500">
            {mode === "login" ? "계정에 로그인하세요." : "간단한 정보로 가입하세요."}
          </p>

          <form action={formAction} className="mt-6 space-y-4">
            <input type="hidden" name="next" value={next} />

            {mode === "signup" && (
              <>
                <label className="block">
                  <span className="text-sm font-semibold text-slate-700">이름</span>
                  <input name="name" required className={cls} placeholder="홍길동" />
                </label>
                <label className="block">
                  <span className="text-sm font-semibold text-slate-700">연락처</span>
                  <input name="phone" className={cls} placeholder="010-0000-0000" />
                </label>
              </>
            )}

            <label className="block">
              <span className="text-sm font-semibold text-slate-700">이메일</span>
              <input name="email" type="email" required className={cls} placeholder="you@example.com" />
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-slate-700">비밀번호</span>
              <input name="password" type="password" required className={cls} placeholder="6자 이상" />
            </label>

            {state?.error && (
              <p className="rounded-lg bg-rose-50 px-3 py-2 text-sm font-semibold text-rose-600">{state.error}</p>
            )}

            <button
              type="submit"
              disabled={pending}
              className="w-full rounded-xl bg-brand-500 py-3 font-bold text-white transition hover:bg-brand-600 disabled:opacity-60"
            >
              {pending ? "처리 중..." : mode === "login" ? "로그인" : "가입하기"}
            </button>
          </form>

          <p className="mt-5 text-center text-sm text-slate-500">
            {mode === "login" ? (
              <>계정이 없으신가요? <Link href="/signup" className="font-bold text-brand-600 hover:underline">회원가입</Link></>
            ) : (
              <>이미 계정이 있으신가요? <Link href="/login" className="font-bold text-brand-600 hover:underline">로그인</Link></>
            )}
          </p>
        </div>
      </div>
    </div>
  );
}
