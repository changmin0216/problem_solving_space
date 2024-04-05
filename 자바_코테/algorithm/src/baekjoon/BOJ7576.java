package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ7576 {
    public static int m;
    public static int n;
    public static Queue<int[]> q = new LinkedList<>();

    public static int[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        map = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    q.add(new int[]{i, j});
                }
            }
        }

        bfs();

        if (check()){
            System.out.println(-1);
        }
        else{
            int result = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    result = Math.max(result, map[i][j]);
                }
            }
            System.out.println(result-1);
        }
    }

    private static boolean check() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    return true;
                }
            }
        }
        return false;
    }

    private static void bfs(){
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        while (!q.isEmpty()) {
            int[] w = new int[2];
            w = q.poll();
            int ey = w[0];
            int ex = w[1];

            for (int i = 0; i < 4; i++) {
                int ny = ey + dy[i];
                int nx = ex + dx[i];

                if ((0 <= ny && ny < n) && (0 <= nx && nx < m)) {
                    if (map[ny][nx] == 0) {
                        map[ny][nx] = map[ey][ex] + 1;
                        q.add(new int[]{ny, nx});
                    }
                }
            }
        }
    }
}
