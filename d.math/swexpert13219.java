import java.util.Scanner;

public class swexpert13219 {
    private Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        swexpert13219 s = new swexpert13219();
        s.solve();
    }

    private void solve() {
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            testcase(i);
        }
    }

    private void testcase(int t) {
        int result = 0;
        int P = sc.nextInt();
        int X = sc.nextInt();
        int Y = sc.nextInt();

        result = isBlack(P, X, Y);
        System.out.println("#"+(t+1)+" "+result);
    }

    private int isBlack(int P, int X, int Y) {
        double x = (double)X-50.0F;
        double y = (double)Y-50.0F;

        double length = Math.sqrt(x * x + y * y);
        if (length > 50.0F) { return 0; }

        double t = Math.atan2(y, x);
        t = t < 0? Math.PI*2+t: t;
        double td = Math.toDegrees(t);
        double pd = (double)P / 100 * 360;

        if (td < 90.0F) { td = 90.0F - td; }
        else { td = 450.0F - td; }
        
        if (td == 0.0F || td == 360.0F) { return 1; }
        if (pd < td) { return 0; }
        return 1;
    }
}
