import java.lang.*;
import java.util.*;
import java.io.*;


public class boj2075 {
    int N;
    PriorityQueue<Integer> pq;

    void addpq(int num) {
        pq.offer(num);
        if (pq.size() > N) {
            pq.poll();
        }
    }

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            String[] split = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                int cur = Integer.parseInt(split[j]);
                addpq(cur);
            }
        }
        System.out.println(pq.poll());
    }

    public static void main(String[] args) {
        try {
            new boj2075().solve();
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}