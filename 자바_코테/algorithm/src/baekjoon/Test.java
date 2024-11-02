package baekjoon;

import java.io.*;
import java.util.*;

public class Test {
    static int n, m, v;
    static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) throws IOException {
        String str1 = "abcd";
        String str2 = "asd";
        if (str1.equals(str2)) { //문자열은 같은 객체 참조
            System.out.println("Equal");
        }

        String str = new String("abcd");
        if (str.equals(str1)) {
            System.out.println("Equal");
        }

        StringBuilder sb = new StringBuilder("Hello");
        System.out.println(sb.toString());
    }
}
