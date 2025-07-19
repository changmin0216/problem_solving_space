package swea;

import java.io.*;
import java.util.*;

public class Solution_7733_d4 {
    static class Point {
        int y, x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    static int N;
    static int[][] chz;
    static boolean[][] visited;
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src/swea/res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            chz = new int[N][N];
            int max_num = 0;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < N; j++) {
                    chz[i][j] = Integer.parseInt(st.nextToken());
                    if (chz[i][j] > max_num) max_num = chz[i][j];
                }
            }

            int result = 0;
            for (int day = 0; day <= max_num; day++) {
                eatChz(day);

                visited = new boolean[N][N];
                int cnt = 0;
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if (chz[i][j] != 0 && !visited[i][j]) {
                            bfs(i, j);
                            cnt+=1;
                        }
                    }
                }
                if (cnt > result) result = cnt;
            }
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    static void eatChz(int day) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (chz[i][j] == day) chz[i][j] = 0;
            }
        }
    }

    static void bfs(int y, int x) {
        ArrayDeque<Point> queue = new ArrayDeque<>();
        queue.offer(new Point(y, x));
        visited[y][x] = true;

        while (!queue.isEmpty()) {
            Point now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];

                if (0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && chz[ny][nx]!=0) {
                    visited[ny][nx] = true;
                    queue.offer(new Point(ny, nx));
                }
            }
        }
    }
}
