import Link from "next/link";

export function PageHero({
  title,
  subtitle,
  crumb,
}: {
  title: string;
  subtitle?: string;
  crumb?: string;
}) {
  return (
    <div className="border-b border-slate-200 bg-gradient-to-br from-brand-600 to-brand-500 text-white">
      <div className="mx-auto max-w-6xl px-5 py-14">
        {crumb && <p className="text-sm font-semibold text-brand-100">{crumb}</p>}
        <h1 className="mt-1 text-3xl font-extrabold tracking-tight">{title}</h1>
        {subtitle && <p className="mt-2 max-w-2xl text-brand-100">{subtitle}</p>}
      </div>
    </div>
  );
}

export function Section({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return <section className={`mx-auto max-w-6xl px-5 py-12 ${className}`}>{children}</section>;
}

export function Badge({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <span className={`inline-block rounded-full px-2.5 py-0.5 text-xs font-bold ${className}`}>
      {children}
    </span>
  );
}

export function Button({
  href,
  children,
  variant = "primary",
  type,
  className = "",
}: {
  href?: string;
  children: React.ReactNode;
  variant?: "primary" | "ghost" | "outline";
  type?: "submit" | "button";
  className?: string;
}) {
  const base =
    "inline-flex items-center justify-center rounded-xl px-5 py-2.5 text-sm font-bold transition";
  const styles = {
    primary: "bg-brand-500 text-white hover:bg-brand-600",
    ghost: "text-slate-700 hover:bg-slate-100",
    outline: "border border-slate-300 text-slate-700 hover:bg-slate-50",
  }[variant];
  const cls = `${base} ${styles} ${className}`;
  if (href) return <Link href={href} className={cls}>{children}</Link>;
  return <button type={type ?? "button"} className={cls}>{children}</button>;
}

export function Field({
  label,
  name,
  type = "text",
  required,
  placeholder,
  defaultValue,
  textarea,
}: {
  label: string;
  name: string;
  type?: string;
  required?: boolean;
  placeholder?: string;
  defaultValue?: string;
  textarea?: boolean;
}) {
  const cls =
    "mt-1.5 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-100";
  return (
    <label className="block">
      <span className="text-sm font-semibold text-slate-700">
        {label} {required && <span className="text-rose-500">*</span>}
      </span>
      {textarea ? (
        <textarea name={name} required={required} placeholder={placeholder} rows={6} defaultValue={defaultValue} className={cls} />
      ) : (
        <input name={name} type={type} required={required} placeholder={placeholder} defaultValue={defaultValue} className={cls} />
      )}
    </label>
  );
}
