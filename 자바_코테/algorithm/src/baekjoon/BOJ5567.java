package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ5567 {
    static int n, m;
    static int[][] graph;
    static int result;

    static void bfs(int start) {
        boolean[] visited = new boolean[n + 1];
        visited[start] = true;

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{start, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            if (0 < cur[1] && cur[1] <= 2) {
                result++;
            }

            for (int i = 1; i < n + 1; i++) {
                if (graph[cur[0]][i] == 1) {
                    if (!visited[i]) {
                        visited[i]=true;
                        q.offer(new int[]{i, cur[1]+1});
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        graph = new int[n + 1][n + 1];

        m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        bfs(1);
        System.out.println(result);
    }
}
