package swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_12712_d2 {
    static int N, M;

    // (상, 하, 좌, 우), (좌상, 좌하, 우하, 우상)
    static int[][] dy = {{-1,1,0,0}, {-1,1,1,-1}};
    static int[][] dx = {{0,0,-1,1}, {-1,-1,1,1}};
    static int[][] matrix;
    static int result;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src/swea/res/input.txt")); //Stream은 바이트 단위로 읽는다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {

            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            matrix = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    matrix[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            result = Integer.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    search(i, j);
                }
            }
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    static void search(int y, int x) {
        for (int d = 0; d < 2; d++) {
            int sum = matrix[y][x];
            for (int i = 0; i < 4; i++) {
                for (int k = 1; k < M; k++) {
                    int ny = y + dy[d][i] * k;
                    int nx = x + dx[d][i] * k;

                    if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                        sum += matrix[y + dy[d][i] * k][x + dx[d][i] * k];
                    }
                }
            }
            if (sum > result) {
                result = sum;
            }
        }
    }
}
