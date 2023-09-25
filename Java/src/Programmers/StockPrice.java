package Programmers;
import java.util.*;

public class StockPrice {
    public int[] solution(int[] prices) {
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < prices.length; i++) {
            int time = 0;
            for (int j = i+1; j < prices.length; j++) {
                time += 1;
                if (prices[i] <= prices[j]) {
                    continue;
                }
                else {
                    break;
                }
            }
            answer.add(time);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
