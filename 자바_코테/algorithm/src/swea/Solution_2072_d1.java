package swea;

import java.io.*;
import java.util.*;

public class Solution_2072_d1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int result = 0;

            for (int i = 0; i < 10; i++) {
                int num = Integer.parseInt(st.nextToken());
                if (num % 2 == 1) {
                    result += num;
                }
            }
            sb.append("#").append(tc + 1).append(" ").append(result).append("\n");

        }
        System.out.print(sb);
    }
}
