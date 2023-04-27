package Programmers;

import java.util.*;

class KthNumber {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();

        for (int[] cmd : commands) {
            int startIndex = cmd[0]-1;
            int endIndex = cmd[1];
            int k = cmd[2]-1;

            int[] slicedArray = Arrays.copyOfRange(array, startIndex, endIndex);

            Arrays.sort(slicedArray);
            answer.add(slicedArray[k]);
        }
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
