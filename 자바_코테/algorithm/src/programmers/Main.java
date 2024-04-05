package programmers;

import java.util.*;

public class Main {
    public static int solution(int[] citations) {
        ArrayList<Integer> answer = new ArrayList<>();

        int max_num = Arrays.stream(citations).max().getAsInt();

        for (int i = 0; i <= max_num; i++) {
            int big = 0, small = 0;
            for (int v : citations) {
                if (v < i) {
                    small+=1;
                }
                else {
                    big+=1;
                }
            }
            if (big >= i && small <=i) {
                answer.add(i);
            }
        }

        for (Integer a : answer) {
            System.out.println(a);
        }
        return Collections.max(answer);
    }
    public static void main(String[] args){
        System.out.println(solution(new int[]{46, 328, 8344, 164, 1}));
//        IntStream.of(solution).forEach(System.out::println);
    }
}
