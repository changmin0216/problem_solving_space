package swea;

import java.io.*;
import java.util.*;

public class Solution_5215_d3 {
    static int T, N, L, result;
    static int[] score;
    static int[] cal;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src/swea/res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());

        for (int tc=1;tc<=T;tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            score = new int[N];
            cal = new int[N];
            for (int i=0;i<N;i++) {
                st = new StringTokenizer(br.readLine());

                score[i] = Integer.parseInt(st.nextToken());
                cal[i] = Integer.parseInt(st.nextToken());
            }
            result = 0;
            dfs(0, 0, 0);
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    public static void dfs(int idx, int calSum, int scoreSum) {
        if (calSum > L) return;

        if (idx>=N) {
            result = Math.max(scoreSum, result);
            return;
        }

        dfs(idx + 1, calSum, scoreSum); //안 먹었을때
        dfs(idx + 1, calSum + cal[idx], scoreSum+score[idx]); //먹었을때
    }
}
