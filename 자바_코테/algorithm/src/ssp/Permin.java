package ssp;

import java.util.Arrays;

public class Permin {
    static int N=4, R=3, C=0;
    static int[] a = {1, 2, 3, 4}, b = new int[3];
    static boolean[] v = new boolean[N];
    static void perm(int cnt) {
        if (cnt==R) {
            System.out.println(Arrays.toString(b));
            C++;
            return;
        }
        for (int i=0;i<N;i++){
            if (v[i]) continue;
            v[i] = true;
            b[cnt] = a[i];
            perm(cnt+1);
            v[i] = false;
        }
    }
    public static void main(String[] args) throws Exception {
        C = 0;
        perm(0);
        System.out.println(C);
    }
}