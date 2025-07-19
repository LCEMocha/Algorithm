import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] times = new int[n][2];

        for (int i = 0; i < n; i++) {
            times[i][0] = sc.nextInt(); // start
            times[i][1] = sc.nextInt(); // end
        }

        Arrays.sort(times, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });

        int count = 0;
        int endTime = 0;

        for (int i = 0; i < n; i++) {
            int start = times[i][0];
            int end = times[i][1];
            if (start >= endTime) {
                count++;
                endTime = end;
            }
        }

        System.out.println(count);
    }
}
