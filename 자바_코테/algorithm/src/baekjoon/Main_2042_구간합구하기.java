package baekjoon;

import java.io.*;
import java.util.*;
public class Main_2042_구간합구하기 {
    static int n, m, k;
    static long[] arr;
    static long[] seg;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new long[n];
        seg = new long[4*n];

        for (int i=0;i<n;i++) {
            arr[i] = Long.parseLong(br.readLine());
        }
        init(1, 0, n - 1);
        for (int i=0;i<m+k;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if(a==1) {
                update(1, 0, n-1, c-arr[b-1], b-1);
            } else {
                System.out.println(query(1, 0, n-1, b-1, ((int)c) - 1));
            }
        }
    }

    static long init(int n, int l, int r) {
        if(l==r) return seg[n] = arr[l];
        int mid = (l+r) / 2;
        seg[n] = init(n*2, l, mid) + init(n*2+1, mid+1, r);
        return seg[n];
    }

    static long query(int n, int seg_s, int seg_e, int arr_s, int arr_e) {
        if (arr_s > seg_e || arr_e < seg_s) return 0;
        if (seg_s >= arr_s && seg_e <= arr_e) return seg[n];
        int mid = (seg_s + seg_e) / 2;
        return query(n*2, seg_s, mid, arr_s, arr_e) + query(n*2+1, mid+1, seg_e, arr_s, arr_e);
    }

    static void update(int n, int s, int e, long diff, int index) {
        if (s > index || index > e) return;
        if (s==e) {
            arr[index]+=diff;
            seg[n]+=diff;
            return;
        }
        int mid = (s+e)/2;
        update(n*2, s, mid, diff, index);
        update(n*2+1, mid+1, e, diff, index);
        seg[n] = seg[n*2] + seg[n*2+1];
    }
}


