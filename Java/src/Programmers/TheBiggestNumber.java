package Programmers;

import java.util.*;

public class TheBiggestNumber {
    public String solution(int[] numbers) {
        String answer = "";
        List<String> nums = new ArrayList<>();

        for (int num : numbers) {
            nums.add(Integer.toString(num));
        }
        Collections.sort(nums, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));

        if (nums.get(0).equals("0")) {
            return "0";
        }

        for (String num : nums) {
            answer += num;
        }

        return answer;
    }
}
