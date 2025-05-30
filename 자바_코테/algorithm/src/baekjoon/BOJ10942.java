package baekjoon;

import java.util.*;
import java.io.*;

public class BOJ10942 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[][] dp = new int[n + 1][n + 1];

        for (int j = 1; j < n + 1; j++) { // 열 먼저 확인
            for (int i = 1; i < j+1; i++) {
                if (i==j) {
                    dp[i][j] = 1;
                }
                else if (j - i == 1) {
                    if (arr[i - 1] == arr[j - 1]) {
                        dp[i][j] = 1;
                    }
                    else{
                        dp[i][j] = 0;
                    }
                }
                else{
                    if ((arr[i - 1] == arr[j - 1]) && (dp[i + 1][j - 1] == 1)) {
                        dp[i][j] = 1;
                    }
                    else{
                        dp[i][j] = 0;
                    }
                }
            }
        }
        int m = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        while(m > 0 ){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(dp[a][b]).append("\n");
            m--;
        }

        System.out.println(sb);
    }
}
