import java.lang.*;
import java.util.*;
import java.io.*;


public class boj7785 {
    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());
        HashSet<String> s = new HashSet<>();

        for (int i = 0; i < N; i++) {
            String[] split = br.readLine().split(" ");
            if (split[1].equals("enter")) {
                s.add(split[0]);
            } else {
                s.remove(split[0]);
            }
        }

        PriorityQueue<String> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (String name : s) { pq.add(name); }
        while (!pq.isEmpty()) {
            System.out.println(pq.poll());
        }
    }

    public static void main(String[] args) {
        try {
            new boj7785().solve();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}