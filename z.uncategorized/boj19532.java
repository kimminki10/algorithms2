import java.lang.*;
import java.util.*;
import java.io.*;


public class boj19532 {

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        int a = Integer.parseInt(split[0]);
        int b = Integer.parseInt(split[1]);
        int c = Integer.parseInt(split[2]);
        int d = Integer.parseInt(split[3]);
        int e = Integer.parseInt(split[4]);
        int f = Integer.parseInt(split[5]);

        for (int x = -999; x <= 999; x++) {
            for (int y = -999; y <= 999; y++) {
                if (a*x+b*y==c && d*x+e*y==f) {
                    System.out.printf("%d %d\n", x, y);
                    return;
                }
            }
        }
    }
    public static void main(String[] args) {
        try {
            new boj19532().solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}