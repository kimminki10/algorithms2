import AuthForm from "@/components/AuthForm";

export const metadata = { title: "회원가입" };

export default function SignupPage() {
  return <AuthForm mode="signup" />;
}
