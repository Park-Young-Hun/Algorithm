package Programmers;

import java.util.*;

public class HateSameNumber {
    public int[] solution(int []arr) {
        int[] answer = {};

        Stack<Integer> stack = new Stack<>();

        for (int num : arr) {
            if (stack.empty()) {
                stack.push(num);
            }
            if (stack.peek() != num) {
                stack.push(num);
            }
        }

        answer = stack.stream()
                .mapToInt(Integer::intValue)
                .toArray();

        return answer;
    }
}
