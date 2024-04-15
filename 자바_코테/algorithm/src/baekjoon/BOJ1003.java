package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ1003 {
    static int one;
    static int zero;
    static Integer[][] dp = new Integer[41][2];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[1][0] = 0;
        dp[1][1] = 1;	

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            fibonacci(n);
            System.out.println(dp[n][0] + " " + dp[n][1]);
        }
    }

    static Integer[] fibonacci(int N) {
        // N에 대한 0, 1의 호출 횟수가 없을 떄(탐색하지 않은 값일 때)
        if(dp[N][0] == null || dp[N][1] == null) {
            // 각 N에 대한 0 호출 횟수와 1 호출 횟수를 재귀호출한다.
            dp[N][0] = fibonacci(N - 1)[0] + fibonacci(N - 2)[0];
            dp[N][1] = fibonacci(N - 1)[1] + fibonacci(N - 2)[1];
        }
        // N에 대한 0과 1, 즉 [N][0]과 [N][1] 을 담고있는 [N]을 반환한다.
        return dp[N];

    }
}
