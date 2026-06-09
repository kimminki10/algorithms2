# 한빛 종합지원센터 — 기관 홈페이지 (MVP)

기관 홈페이지 구축 프로젝트입니다. 로그인, 기관 소개, 공지사항, 온라인 신청(대관·프로그램·사업), FAQ와
관리자 백오피스를 포함합니다.

## 기술 스택

- **Next.js 16** (App Router) + **TypeScript**
- **Tailwind CSS v4**
- **Prisma 6** + **SQLite** (개발/데모) — 배포 시 PostgreSQL(Supabase 등)로 교체 가능
- **JWT 쿠키 인증** (`jose` + `bcryptjs`), 회원/관리자 권한 분리

## 빠른 시작

```bash
npm install            # 의존성 설치 (+ prisma generate)
cp .env.example .env   # 환경변수 준비
npm run db:push        # DB 스키마 생성
npm run db:seed        # 샘플 데이터 + 계정 시드
npm run dev            # http://localhost:3000
```

## 데모 계정 (시드)

| 구분 | 이메일 | 비밀번호 |
|------|--------|----------|
| 관리자 | `admin@hanbit.kr` | `admin1234` |
| 일반 회원 | `user@test.kr` | `test1234` |

관리자로 로그인하면 헤더의 **관리자** 메뉴 또는 `/admin` 으로 백오피스에 접근할 수 있습니다.

## 주요 화면

| 영역 | 경로 | 설명 |
|------|------|------|
| 홈 | `/` | 히어로, 빠른 신청, 최신 공지 |
| 기관소개 | `/about` | 인사말, 현황, 핵심가치, 오시는 길 |
| 공지사항 | `/notices`, `/notices/[id]` | 목록 / 상세(조회수) |
| 신청 | `/apply`, `/apply/[type]` | 대관·프로그램·사업 신청 폼 |
| FAQ | `/faq` | 분류별 아코디언 |
| 마이페이지 | `/mypage` | 내 신청 현황·상태 |
| 인증 | `/login`, `/signup` | 로그인 / 회원가입 |
| 관리자 | `/admin/*` | 대시보드, 신청 승인/반려, 공지·FAQ 관리 |

## 배포 메모

- Vercel 배포 시 환경변수 `DATABASE_URL`, `AUTH_SECRET` 설정
- 운영 DB는 `prisma/schema.prisma` 의 `provider` 를 `postgresql` 로 바꾸고 `prisma migrate deploy`
- `AUTH_SECRET` 은 반드시 운영용 랜덤 값으로 교체
