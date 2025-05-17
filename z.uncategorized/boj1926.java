import java.io.*;
import java.lang.*;
import java.util.*;

class P {
    int x,y;
    public P(int a, int b) {
        this.x=a; this.y=b;
    }
    public boolean equals(Object v) {
        P o = (P)v;
        return o.x == this.x && o.y == this.y;
    }
    public int hashCode() {
        return this.x * 1000 + this.y;
    }
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}

public class boj1926 {

    static int[][] di = {{0,1}, {1,0}, {-1,0}, {0,-1}};

    public static HashSet<P> bfs(int[][] jido, P s) {
        HashSet<P> ans = new HashSet<P>();
        Queue<P> q = new LinkedList<P>();
        ans.add(s);
        q.add(s);

        while (!q.isEmpty()) {
            P cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + di[i][0];
                int ny = cur.y + di[i][1];

                P n = new P(nx, ny);
                if (jido[nx][ny] == 1 && !ans.contains(n)) {
                    q.add(n);
                    ans.add(n);
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] split = line.split(" ");
        int n, m;
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);

        int[][] jido = new int[n+2][m+2];
        for (int i = 0; i < n; i++) {
            line = br.readLine();
            split = line.split(" ");

            for (int j = 0; j < m; j++) {
                int v = Integer.parseInt(split[j]);
                jido[i+1][j+1] = v;
            }
        }
        
        int a = 0, b = 0;
        HashSet<P> s = new HashSet<P>();
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < m+1; j++) {
                if (jido[i][j] == 0) { continue; }
                P np = new P(i, j);
                if (!s.contains(np)) {
                    a += 1;
                    HashSet<P> res = bfs(jido, np);
                    b = res.size() > b ? res.size() : b;
                    s.addAll(res);
                }
            }
        }
        System.out.println(a);
        System.out.println(b);
    }
}