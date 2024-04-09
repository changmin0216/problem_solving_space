package programmers;

import java.util.*;

public class Main {
    public static int solution(int[][] dots) {
        int answer = 0;
        int x1 = dots[0][0];
        int y1 = dots[0][1];
        int x2 = dots[1][0];
        int y2 = dots[1][1];
        int x3 = dots[2][0];
        int y3 = dots[2][1];
        int x4 = dots[3][0];
        int y4 = dots[3][1];

        double slop1 = (double)(y1-y2) / (double)(x1-x2);
        double slop2 = (double)(y3-y4) / (double)(x3-x4);

        double slop3 = (double)(y1-y3) / (double)(x1-x3);
        double slop4 = (double)(y2-y4) / (double)(x2-x4);

        double slop5 = (double)(y1-y4) / (double)(x1-x4);
        double slop6 = (double)(y2-y3) / (double)(x2-x3);

        if ((slop1 == slop2) || (slop3 == slop4) || (slop5==slop6))  {
            answer = 1;
        }

        return answer;
    }
    public static void main(String[] args){
        System.out.println(solution(new int[][]{{1, 4}, {9, 2}, {3, 8}, {11, 6}}));
    }
}
