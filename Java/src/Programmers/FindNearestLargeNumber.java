package Programmers;

public class FindNearestLargeNumber {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            answer[i] = -1;
        }

        for (int i = n-2; i >= 0; i--) {
            if (numbers[i+1] > numbers[i]) {
                answer[i] = numbers[i+1];
                continue;
            }

            for (int j = i+1; j < n; j++) {
                if (answer[j] == -1) {
                    answer[i] = -1;
                    break;
                }

                if (answer[j] > numbers[i]) {
                    answer[i] = answer[j];
                    break;
                }
            }
        }
        return answer;
    }
}
