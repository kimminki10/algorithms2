import java.io.*;
import java.util.*;

public class boj2143 {

    public void subsum(long[] A, long[] B, int n, int m, long[] sumA, long[] sumB) {
        sumA[0] = 0;
        sumB[0] = 0;
        for (int i = 0; i < n; i++) {
            sumA[i+1] = sumA[i] + A[i];
        }
        for (int i = 0; i < m; i++) {
            sumB[i+1] = sumB[i] + B[i];
        }
    }

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        long T = Long.parseLong(input);
        int n = Integer.parseInt(br.readLine());
        long[] A = new long[n];
        String[] str = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            A[i] = Long.parseLong(str[i]);
        }
        int m = Integer.parseInt(br.readLine());
        long[] B = new long[m];
        str = br.readLine().split(" ");
        for (int i = 0; i < m; i++) {
            B[i] = Long.parseLong(str[i]);
        }

        long[] sumA = new long[n+1];
        long[] sumB = new long[m+1];
        subsum(A, B, n, m, sumA, sumB);

        HashMap<Long, Long> HA = new HashMap<>();
        HashMap<Long, Long> HB = new HashMap<>();
        long cnt = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                long ss = sumA[i] - sumA[j];
                if (HA.containsKey(ss)) {
                    HA.put(ss, HA.get(ss) + 1);
                } else {
                    HA.put(ss, 1L);
                }
            }
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 0; j < i; j++) {
                Long ss = sumB[i] - sumB[j];
                if (HB.containsKey(ss)) {
                    HB.put(ss, HB.get(ss) + 1);
                } else {
                    HB.put(ss, 1L);
                }
            }
        }

        for (Long key : HA.keySet()) {
            if (HB.containsKey(T - key)) {
                cnt += HA.get(key) * HB.get(T - key);
            }
        }
        System.out.println(cnt);
    }

    public static void main(String[] args) throws IOException {
        new boj2143().solve();
    }
}
