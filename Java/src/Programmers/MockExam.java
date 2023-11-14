package Programmers;

import java.util.*;

public class MockExam {
    public int[] solution(int[] answers) {
        int maxScore = 0;
        int[][] students = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        List<Integer> answer = new ArrayList<>();

        HashMap<Integer, Integer> studentScore = new HashMap<>();

        for (int i = 0; i < students.length; i++) {
            studentScore.put(i+1, 0);
        }

        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < students.length; j++) {
                if (answers[i] == students[j][i % students[j].length]) {
                    int newScore = studentScore.get(j+1) + 1;

                    if (newScore > maxScore) {
                        maxScore = newScore;
                    }
                    studentScore.put(j+1, newScore);
                }
            }
        }

        for (Integer key: studentScore.keySet()) {
            if (studentScore.get(key) == maxScore) {
                answer.add(key);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
