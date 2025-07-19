package swea;

import java.io.*;
import java.util.*;

public class Solution_1959_d2 {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src/swea/res/input.txt")); //Stream은 바이트 단위로 읽는다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N, M;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            int[] A = new int[N];
            int[] B = new int[M];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                B[i] = Integer.parseInt(st.nextToken());
            }

            int num = Math.min(N, M);

            int result = Integer.MIN_VALUE;
            if (num == N) {
                for (int idx = 0; idx <= M - N; idx++) {
                    int sum = 0;
                    for (int i = 0; i < num; i++) {
                        sum += A[i] * B[i+idx];
                    }
                    if (sum > result) {
                        result = sum;
                    }
                }
            }
            else {
                for (int idx = 0; idx <= N - M; idx++) {
                    int sum = 0;
                    for (int i = 0; i < num; i++) {
                        sum += A[i+idx] * B[i];
                    }
                    if (sum > result) {
                        result = sum;
                    }
                }
            }
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
