package leetcode;

import java.util.Arrays;

public class Lc217ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        // nums 안에 중복되는 정수가 있으면 true, 중복되는 값이 없으면 false
        Arrays.sort(nums);

        int num = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (num == nums[i]) {
                return true;
            }
            num = nums[i];
        }
        return false;
    }
    public static void main(String[] args) {
        Lc217ContainsDuplicate sol = new Lc217ContainsDuplicate();
        System.out.println(sol.containsDuplicate(new int[]{1,1,1,3,3,4,3,2,4,2}));
    }
}