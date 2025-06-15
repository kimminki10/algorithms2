import java.lang.*;
import java.util.*;
import java.io.*;


public class boj9506 {

    void evaluate(int num) {
        int accumulate = 0;
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                accumulate += i;
                arr.add(String.valueOf(i));
            }
        }

        if (accumulate == num) {
            String args = String.join(" + ", arr);
            System.out.printf("%d = %s\n", num, args);
        } else {
            System.out.println(num+" is NOT perfect.");
        }
    }

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int cur = Integer.parseInt(br.readLine().trim());
            if (cur == -1) { break; }
            evaluate(cur);
        }
    }

    public static void main(String[] args) {
        try {
            new boj9506().solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}