package baemin;

import java.util.*;

public class Second {
    static int x,y;
    static int ans;
    public static int solution(int n, int a, int b){
        int answer = 0;

        ArrayList<Integer> ary = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            ary.add(i);
        }

        x = a;
        y = b;
        ans=0;
        recur(ary, 1);
        return ans;
    }

    public static void recur(ArrayList<Integer> ary, int depth){
        if (ary.size()==2){
            return;
        }

        for (int i=0;i<ary.size();i+=2){
            int a = ary.get(i);
            int b = ary.get(i + 1);

            //둘다 a 또는 b 일때
            if ((a==x || a==y) && (b==x || b==y)){
                return;
            }

            //둘다 a 또는 b가 아닐 때
            else if ((a!=x || a!=y) && (b!=x || b!=y)){
                ary.remove(i);
            }

            //둘개 중 하나가 a 또는 b일때
            else{
                if (a==x || a==y){
                    ary.remove(i+1);
                } else ary.remove(i);
            }
        }
        ans+=1;
        recur(ary, depth+1);
    }
    public static void main(String[] args){
        System.out.println(solution(8,4,7));

    }
}
