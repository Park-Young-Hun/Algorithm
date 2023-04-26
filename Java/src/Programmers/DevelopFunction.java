package Programmers;

import java.util.*;

class DevelopFunction {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> deployDays = new ArrayDeque<>();

        for (int i = 0; i < progresses.length; i++) {
            int day = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]); //소요 일수 계산.

            if (deployDays.isEmpty()) {
                deployDays.add(day);
                continue;
            }

            if (deployDays.element() >= day) {
                deployDays.add(day);
            }
            else {
                answer.add(deployDays.size());
                deployDays.clear();
                deployDays.add(day);
            }
        }

        if (!deployDays.isEmpty()) {
            answer.add(deployDays.size());
        }

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
