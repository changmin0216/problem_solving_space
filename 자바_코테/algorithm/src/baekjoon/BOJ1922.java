package baekjoon;

import java.util.*;
import java.io.*;

public class BOJ1922 {
    static ArrayList<int[]> edges;
    static int n;
    static int m;
    static int result = 0;
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] s = br.readLine().split(" ");
            int[] tmp = {Integer.parseInt(s[0]), Integer.parseInt(s[1]), Integer.parseInt(s[2])};
            edges.add(tmp);
        }
        edges.sort((o1, o2) -> {
            return o1[2]-o2[2]; //양수 반환 --> 순서 바꿈
        });

        parent = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < m; i++) {
            int[] tmp = edges.get(i);
            if (find_parent(parent, tmp[0]) != find_parent(parent, tmp[1])) {
                result += tmp[2];
                union_parent(parent, tmp[0], tmp[1]);
            }
        }
        System.out.println(result);
    }

    static private int find_parent(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find_parent(parent, parent[x]);
        }
        return parent[x];
    }

    static private void union_parent(int[] parent, int a, int b) {
        a = find_parent(parent, a);
        b = find_parent(parent, b);

        if (a < b) {
            parent[b] = a;
        }
        else {
            parent[a] = b;
        }
    }

}
