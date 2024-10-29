package baekjoon;

import java.util.*;
import java.io.*;

public class BOJ14889 {
    static int n; //짝수
    static int[][] list;
    static ArrayList<Integer> result;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        list = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                list[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        result = new ArrayList<>();
        recur(new ArrayList<>(), 0);
        System.out.println(Collections.min(result));
    }
    static void recur(ArrayList<Integer> tmp, int index){
        if (tmp.size() == n / 2) {
            boolean[] visited = new boolean[n];
            for (int num: tmp){
                visited[num] = true;
            }
            int sum = 0;
            for (int i = 0; i < n - 1; i++) {
                for (int j = i+1; j < n;j++) {
                    if ((visited[i]) && (visited[j])){
                        sum+=(list[i][j]+list[j][i]);
                    }
                    else if((!visited[i]) && (!visited[j])){
                        sum-=(list[i][j]+list[j][i]);
                    }
                }
            }
            result.add(Math.abs(sum));
            return;
        }
        for (int i = index; i < n; i++) {
            tmp.add(i);
            recur(tmp, i+1);
            tmp.remove(tmp.size()-1);
        }
    }
}
