import java.util.Scanner;

public class swexpert13240 {
    private Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        swexpert13240 s = new swexpert13240();
        s.solve();
    }

    private void solve() {
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            testcase(i);
        }
    }

    private void testcase(int i) {
        int result = 0;
        int H = 0, W = 0, N = 0;
        String s = "";

        H = sc.nextInt();
        W = sc.nextInt();
        N = sc.nextInt(); sc.nextLine();
        s = sc.nextLine();
        s = s.trim();

        result = biggestSize(H, W, N, s);
        System.out.println("#"+(i+1)+" "+result);
    }
    
    private int biggestSize(int H, int W, int N, String line) {
        String[] sarr = line.split(" ");
        
        int l = 0, r = H > W? H: W, m, ans = -1;
        while (l <= r) {
            m = (l+r) / 2;
            if (isPossible(sarr, H, W, N, m)) {
                ans = m;
                l = m + 1;
            }
            else r = m - 1;
        }

        return ans;
    }

    private boolean isPossible(String[] sarr, int H, int W, int N, int m) {
        int h = H / m, w = W / m;
        int lc = w;
        int hc = h;
        for (int i = 0; i < N; i++) {
            if (w < sarr[i].length()) { return false; }
            if (hc == 0) { return false; }
            
            if (lc != w) { lc -= 1; }
            if (lc >= sarr[i].length()) {
                lc -= sarr[i].length();
            } else {
                i--;
                lc = w;
                hc--;
            }
        }
        return true;
    }
}
