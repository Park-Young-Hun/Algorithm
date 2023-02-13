package Programmers;

import java.util.*;

public class Ponkemon {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> kind = new HashSet<>();

        for(int num : nums) {
            kind.add(num);
        }

        if(nums.length / 2 > kind.size()) {
            answer = kind.size();
        }
        else {
            answer = nums.length / 2;
        }

        return answer;
    }
}
