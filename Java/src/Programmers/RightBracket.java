package Programmers;

import java.util.*;

class RightBracket {
    boolean solution(String s) {
        boolean answer = true;
        Deque<String> stack = new ArrayDeque<>();

        for (char chr : s.toCharArray()) {
            if (chr == '(') {
                stack.push(String.valueOf(chr));
                continue;
            }
            if (!stack.isEmpty()) {
                stack.pop();
                continue;
            }
            return false;
        }

        return stack.isEmpty();
    }
}
