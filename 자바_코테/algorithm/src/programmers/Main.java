package programmers;

import java.util.*;

public class Main {
    public static int solution(int n, int[] lost, int[] reserve) {
        int[] student = new int[n+1];
        for(int i=0;i<lost.length;i++){
            student[lost[i]] = -1;
        }
        for(int i=0;i<reserve.length;i++){
            student[reserve[i]]+=1;
        }

        for(int i=1;i<n+1;i++){
            if (student[i] == -1){
                if (student[i-1]>0){
                    student[i]+=1;
                    student[i-1]-=1;
                    continue;
                }
                if (i!=n) {
                    if (student[i + 1] > 0) {
                        student[i] += 1;
                        student[i + 1] -= 1;
                    }
                }
            }
        }
        int answer = 0;
        for (int i=1;i<n+1;i++){
            if (student[i]>=0){
                answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        System.out.println(solution(3,new int[]{3}, new int[]{1}));
    }
}
