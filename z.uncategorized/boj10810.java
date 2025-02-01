import java.util.Scanner;

public class boj10810 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N, M;
        N = sc.nextInt();
        M = sc.nextInt();

        int[] arr = new int[N];

        for (int x = 0; x < M; x++) {
            int i, j, k;
            i = sc.nextInt();
            j = sc.nextInt();
            k = sc.nextInt();
            
            for (int y = i - 1; y < j; y++) {
                arr[y] = k;
            }
        }

        for (int x = 0; x < N; x++) {
            System.out.print(arr[x] + " ");
        }
    }
}
