import { PrismaClient } from "../src/generated/prisma";
import bcrypt from "bcryptjs";

const prisma = new PrismaClient();

async function main() {
  // 기존 데이터 정리
  await prisma.application.deleteMany();
  await prisma.notice.deleteMany();
  await prisma.faq.deleteMany();
  await prisma.user.deleteMany();

  const adminPw = await bcrypt.hash("admin1234", 10);
  const userPw = await bcrypt.hash("test1234", 10);

  const admin = await prisma.user.create({
    data: { email: "admin@hanbit.kr", password: adminPw, name: "관리자", role: "ADMIN" },
  });

  const member = await prisma.user.create({
    data: { email: "user@test.kr", password: userPw, name: "홍길동", phone: "010-1234-5678", role: "USER" },
  });

  await prisma.notice.createMany({
    data: [
      { title: "[중요] 2026년 상반기 시설 대관 안내", content: "2026년 상반기 시설 대관 신청을 받습니다.\n\n- 신청 기간: 2026.06.01 ~ 06.30\n- 대상 시설: 대강당, 세미나실, 다목적홀\n- 신청 방법: 홈페이지 온라인 신청\n\n자세한 사항은 담당자에게 문의해 주세요.", pinned: true, views: 152, authorId: admin.id },
      { title: "여름방학 특별 교육 프로그램 모집", content: "지역 주민을 위한 여름방학 특별 교육 프로그램 참가자를 모집합니다.\n\n다양한 강좌가 준비되어 있으니 많은 참여 바랍니다.", views: 88, authorId: admin.id },
      { title: "홈페이지 리뉴얼 오픈 안내", content: "더욱 편리해진 새 홈페이지가 오픈했습니다. 온라인 신청 기능을 이용해 보세요.", views: 240, authorId: admin.id },
      { title: "센터 운영시간 변경 안내", content: "2026년 6월부터 센터 운영시간이 평일 09:00 ~ 21:00 으로 변경됩니다.", views: 61, authorId: admin.id },
    ],
  });

  await prisma.faq.createMany({
    data: [
      { category: "대관", question: "시설 대관은 어떻게 신청하나요?", answer: "홈페이지 상단 '신청 > 대관 신청'에서 온라인으로 신청하실 수 있습니다. 신청 후 담당자 승인을 거쳐 확정됩니다.", sort: 1 },
      { category: "대관", question: "대관 취소 및 환불 규정이 궁금합니다.", answer: "이용일 7일 전까지 취소 시 전액 환불, 이후에는 규정에 따라 차등 환불됩니다.", sort: 2 },
      { category: "프로그램", question: "프로그램 수강료는 어떻게 결제하나요?", answer: "신청 접수 후 안내되는 계좌로 입금하시면 됩니다. 일부 프로그램은 무료로 운영됩니다.", sort: 1 },
      { category: "회원", question: "회원가입은 필수인가요?", answer: "비회원도 신청이 가능하지만, 회원가입 시 마이페이지에서 신청 현황을 편리하게 확인할 수 있습니다.", sort: 1 },
      { category: "일반", question: "운영시간과 휴관일은 어떻게 되나요?", answer: "평일 09:00 ~ 21:00 운영하며, 매주 일요일과 법정 공휴일은 휴관합니다.", sort: 1 },
    ],
  });

  await prisma.application.createMany({
    data: [
      { type: "RENTAL", title: "동아리 정기모임 세미나실 대관", applicantName: "홍길동", phone: "010-1234-5678", email: "user@test.kr", desiredDate: "2026-06-20", content: "주말 동아리 정기모임을 위해 세미나실을 대관하고자 합니다. 20명 내외입니다.", status: "PENDING", userId: member.id },
      { type: "PROGRAM", title: "여름 코딩교실 참가 신청", applicantName: "김영희", phone: "010-2222-3333", email: "kim@test.kr", content: "초등학생 자녀의 코딩교실 참가를 신청합니다.", status: "APPROVED" },
      { type: "BUSINESS", title: "청년 창업 지원사업 신청", applicantName: "박철수", phone: "010-4444-5555", email: "park@test.kr", content: "청년 창업 지원사업에 지원하고자 합니다. 사업계획서는 별도 제출 예정입니다.", status: "PENDING" },
    ],
  });

  console.log("✅ Seed 완료");
  console.log("   관리자: admin@hanbit.kr / admin1234");
  console.log("   회원:   user@test.kr / test1234");
}

main()
  .catch((e) => { console.error(e); process.exit(1); })
  .finally(() => prisma.$disconnect());
