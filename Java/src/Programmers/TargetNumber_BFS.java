package Programmers;

import java.util.*;

class TargetNumber_BFS {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        int start = 0;

        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(start);

        for (int num : numbers) {
            int len = queue.size();

            for (int i = 0; i < len; i++) {
                int val = queue.remove();

                queue.add(val + num);
                queue.add(val - num);
            }
        }

        while (!queue.isEmpty()) {
            int val = queue.remove();

            if (val == target) {
                answer++;
            }
        }
        return answer;
    }
}
