import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class swexpert13041 {
    private Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        swexpert13041 s = new swexpert13041();
        s.solve();
    }

    private void solve() {
        long t = sc.nextInt();
        for (long i = 0; i < t; i++) {
            testcase(i);
        }
    }

    private void testcase(long t) {
        int N = sc.nextInt(); // 게으른 사람 수
        int K = sc.nextInt(); // 중요한 일의 수

        int[] arr = new int[N]; // i번째 사람이 고른 일
        long[] brr = new long[N]; // i번째 사람을 설득하기 위해 필요한 시간
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            brr[i] = sc.nextInt();
        }

        long result = minTime(arr, brr, N, K);
        System.out.println("#"+(t+1)+" "+result);
    }

    private long minTime(int[] arr, long[] brr, int N, int K) {
        ArrayList< PriorityQueue<Long> > works = new ArrayList<>(K);
        PriorityQueue<Long> extra = new PriorityQueue<>();
        for (int i = 0; i < K; i++) {
            works.add(new PriorityQueue<Long>());
        }

        for (int i = 0; i < N; i++) {
            PriorityQueue<Long> w = works.get(arr[i]-1);
            if (!w.isEmpty()) {
                w.add(brr[i]);
                extra.add(w.poll());
            } else {
                w.add(brr[i]);
            }
        }

        long emptyCount = 0;
        for (PriorityQueue<Long> w : works) {
            if (w.isEmpty()) { emptyCount += 1; }
        }

        long result = 0;
        for (long i = 0; i < emptyCount; i++) {
            result += extra.poll();
        }

        return result;
    }
}