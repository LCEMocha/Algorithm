import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 동전 종류 수
        int K = sc.nextInt(); // 목표 금액

        int[] coins = new int[N];
        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        int count = 0;

        // 큰 동전부터 사용
        for (int i = N - 1; i >= 0; i--) {
            if (coins[i] <= K) {
                int cnt = K / coins[i];
                count += cnt;
                K -= coins[i] * cnt;
            }
        }

        System.out.println(count);
    }
}