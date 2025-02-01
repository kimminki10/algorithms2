import java.util.Scanner;

class boj11312 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            System.out.println((long) Math.pow(a / b, 2));
        }

        sc.close();
    }
}