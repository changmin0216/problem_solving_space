package swea;

import java.io.*;
import java.util.*;

public class Solution_1961_d2 {
    static int N;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src/swea/res/input.txt")); //Stream은 바이트 단위로 읽는다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            int[][] matrix;
            matrix = new int[N][N];

            String[][] result = new String[N][3];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    matrix[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int j = 0; j < 3; j++) {
                matrix = rotateMatrix90(matrix);

                String[] tmp = new String[N];
                for (int y = 0; y < N; y++) {
                    StringBuilder s = new StringBuilder();
                    for (int x = 0; x < N; x++) {
                        s.append(matrix[y][x]);
                    }
                    tmp[y] = s.toString();
                }

                for (int i = 0; i < N; i++) {
                    result[i][j] = tmp[i];
                }
            }
            System.out.println("#" + tc);
            for (String[] row : result) {
                for (String s : row) {
                    System.out.print(s + " ");
                }
                System.out.println();
            }
        }
    }

    static int[][] rotateMatrix90(int[][] matrix) {
        int[][] rotate_matrix = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                rotate_matrix[j][N-1-i] = matrix[i][j];
            }
        }
//        for (int[] a:rotate_matrix) System.out.println(Arrays.toString(a));
        return rotate_matrix;
    }
}
