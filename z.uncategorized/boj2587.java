import java.lang.*;
import java.util.*;
import java.io.*;


public class boj2587 {

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();

        int s = 0;
        for (int i = 0; i < 5; i++) {
            int cur = Integer.parseInt(br.readLine().trim());
            s += cur;
            arr.add(cur);
        }
        arr.sort(Comparator.naturalOrder());
        System.out.printf("%d\n%d\n", s/5, arr.get(2));
    }
    public static void main(String[] args) {
        try {
            new boj2587().solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}