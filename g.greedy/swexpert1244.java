import java.util.Scanner;

public class swexpert1244 {
    Scanner sc = new Scanner(System.in);
    int num = 0;
    int numLength = 0;
    int best = 0;
    int change = 0;

    int max(int a, int b) {
        return a > b? a: b;
    }

    void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    int[] intToArr(int n){
        int[] result = new int[numLength];
        for (int i = 0; n != 0; n = n / 10, i++) {
            result[i] = n % 10;
        }
        return result;
    }

    int arrToInt(int[] arr) {
        int result = 0;
        for (int i = numLength-1; i >= 0; i--) {
            result = result * 10 + arr[i];
        }
        return result;
    }

    void maxValue(int[] n, int now, int depth) {
        if (depth == change) { 
            best = max(best, arrToInt(n));
            return; 
        }
        for (int i = now; i < numLength; i++) {
            for (int j = i+1; j < numLength; j++) {
                if (n[i] >= n[j]) {
                    swap(n, i, j);
                    maxValue(n, i, depth+1);
                    swap(n, i, j);
                }
            }
        }
        
        swap(n, 0, 1);
        maxValue(n, now, depth+1);
        swap(n, 0, 1);
    }

    boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length-1; i++) {
            if (arr[i] < arr[i+1]) {
                return false;
            }
        }
        return true;
    }

    void testcase(int i) {
        num = sc.nextInt();
        change = sc.nextInt();
        best = 0;
        for (int r = num, j=1; r != 0; r /=10, j++){
            numLength = j;
        }
        if (change > numLength) {
            change = numLength + (change % numLength);
        }
        int[] numArr = intToArr(num);
        maxValue(numArr, 0, 0);
        
        System.out.println("#"+(i+1)+" "+best);
    }

    void solve() {
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            testcase(i);
        }
        sc.close();
    }

    public static void main(String[] args) {
        swexpert1244 m = new swexpert1244();
        m.solve();
    }
}