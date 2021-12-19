import java.io.*;
import java.util.*;

/* 
 * https://www.acmicpc.net/problem/15552
 * 빠른 A+B
 * 빠른 입출력을 해본다.
 */

/**
 * boj15552
 */
public class boj15552 {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    public void solve() throws IOException {
        int t = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            bw.write(a+b+"\n");
        }
        
        bw.flush();
    }
    public static void main(String[] args) throws IOException {
        boj15552 m = new boj15552();
        m.solve();
    }
}