package programmers;

import java.util.*;

public class Main {
    static int answer;
    static int[] number;
    static int size;
    public static int solution(int[] numbers, int target) {
        answer = 0;
        number = numbers;
        size = numbers.length;

        dfs(0, 0, target);
        return answer;
    }

    public static void dfs(int depth, int sum, int target){
        if (depth==size){
            if (sum==target){
                answer++;
            }
            return;
        }

        dfs(depth+1, sum+number[depth], target);
        dfs(depth+1, sum-number[depth], target);
    }

    public static void main(String[] args){
        System.out.println(solution(new int[]{1,1,1,1,1}, 3));
    }
}
