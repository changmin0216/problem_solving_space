package ssafy;

import java.io.*;
import java.util.*;

public class Solution_1289_d3_원재의메모리복구하기{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            String memory = br.readLine();

            int cnt = 0;
            char currentBit = '0';
            for (int i = 0; i < memory.length(); i++) {
                if (memory.charAt(i) != currentBit) {
                    cnt += 1;
                    currentBit = memory.charAt(i);
                }
            }
            sb.append("#").append(tc).append(" ").append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}
