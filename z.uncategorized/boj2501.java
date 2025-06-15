import java.io.*;
import java.util.*;
import java.lang.*;

public class boj2501 {
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    int N = 0, K = 0;
    void addpq(int num) {
        pq.offer(num);
        if (pq.size() > K) {
            pq.poll();
        }
    }
    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));   
        String[] split = br.readLine().split(" ");
        N = Integer.parseInt(split[0]);
        K = Integer.parseInt(split[1]);

        for (int i = 1; i <= N; i++) {
            if ((N % i) == 0) {
                addpq(i);
            }
        }
        int answer = 0;
        if (pq.size() == K) { answer = pq.peek();}
        System.out.println(answer);
    }

    public static void main(String[] args) {
        try {
            new boj2501().solve();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}