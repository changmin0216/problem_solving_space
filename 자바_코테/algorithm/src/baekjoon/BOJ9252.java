package baekjoon;

import java.io.*;
import java.util.*;
public class BOJ9252 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();

        int[][] dp = new int[str1.length()+1][str2.length()+1];

        for (int i = 1; i < str1.length()+1; i++) {
            for (int j = 1; j < str2.length() + 1; j++) {
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); //만약 다르다면 i-1번 째 값과 j-1번째 값을 비교해서 다 큰 값을 작용
                }
            }
        }
//        System.out.println(Arrays.toString(dp[0]));
//        Arrays.fill(dp[0], -1);
//        System.out.println(Arrays.toString(dp[0]));
//        for (int i = 0; i < str1.length() + 1; i++) {
//            System.out.println(Arrays.toString(dp[i]));
//        }

        StringBuilder sb = new StringBuilder();

        int i = str1.length();
        int j = str2.length();

        while (i > 0 && j > 0) {
            // 뒤 부터 확인해서 같으면 --> 결과 값에 추가
            if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                sb.append(str1.charAt(i - 1));
                i--;
                j--;
            }
            // 다르면 dp[i-1][j]랑 dp[i][j-1] 중 더 큰 값을 비교한다.
            else {
                if (dp[i - 1][j] > dp[i][j - 1]) {
                    i--;
                } else {
                    j--;
                }
            }
        }

        if (dp[str1.length()][str2.length()] == 0) {
            System.out.println(0);
        }
        else{
            System.out.println(dp[str1.length()][str2.length()]);
            System.out.println(sb.reverse());
        }
    }
}
