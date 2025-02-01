import java.io.*;
import java.util.*;
import java.lang.*;

public class boj12021 {

    public static double nextX(double x, double y) {
        return (x+y) / 2;
    }

    public static double nextY(double x, double y) {
        return 2 * x * y / (x + y);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] line = br.readLine().split(" ");

        double a = Double.parseDouble(line[0]);
        double b = Double.parseDouble(line[1]);

        while (true) {
            double x = nextX(a, b);
            double y = nextY(a, b);

            if (x == a && y == b) {
                break;
            }

            a = x;
            b = y;
        }
        sb.append(String.format("%.3f %.3f", a, b));
        System.out.println(sb);
    }
}
