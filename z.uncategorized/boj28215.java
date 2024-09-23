import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class boj28215 {
    public static int N, K;
    public static int[] idxs = new int[10];
    public static int idxidx = 0;
    public static int[] xarr = new int[100001];
    public static int[] yarr = new int[100001];
    public static int ans = 987654321;

    public static int dist(int a, int b, int x, int y) {
        return Math.abs(a-x)+Math.abs(b-y);
    }
    
    public static void solve() {
        int maxd = 0;
        for (int i = 0; i < N; i++) {
            int x = xarr[i];
            int y = yarr[i];

            int mind = 987654321;
            for (int j = 0; j < K; j++) {
                int idx = idxs[j];
                int a = xarr[idx];
                int b = yarr[idx];

                int d = dist(a,b,x,y);
                mind = Math.min(d, mind);
            }
            maxd = Math.max(maxd, mind);
        }
        ans = Math.min(maxd, ans);
    }

    public static void dfs(int idx, int d) {
        if (d == K) {
            solve();
            return;
        }

        for (int i = idx+1; i < N; i++) {
            idxs[idxidx++] = i;
            dfs(i, d+1);
            idxidx--;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] line = bf.readLine().trim().split(" ");
        N = Integer.parseInt(line[0]);
        K = Integer.parseInt(line[1]);

        xarr = new int[100001];
        yarr = new int[100001];

        for (int i = 0; i < N; i++) {
            line = bf.readLine().trim().split(" ");
            xarr[i] = Integer.parseInt(line[0]);
            yarr[i] = Integer.parseInt(line[1]);
        }

        dfs(-1, 0);

        bw.write(""+ans);
        bw.flush();
        bw.close();
        bf.close();
    }
}