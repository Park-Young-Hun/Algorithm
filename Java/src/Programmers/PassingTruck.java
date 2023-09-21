package Programmers;

import java.util.*;

class PassingTruck {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        int curWeight = 0;
        Deque<Integer> bridge = new ArrayDeque<>();
        Deque<Integer> trucks = new ArrayDeque<>();

        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        for (int truck : truck_weights) {
            trucks.add(truck);
        }

        int truck = trucks.remove();
        bridge.remove();
        bridge.add(truck);
        curWeight += truck;
        time++;

        while (curWeight > 0) {
            if (!trucks.isEmpty() && curWeight + trucks.element() - bridge.element() <= weight) {
                truck = trucks.remove();
                curWeight -= bridge.remove();
                bridge.add(truck);
                curWeight += truck;
            }
            else {
                curWeight -= bridge.remove();
                bridge.add(0);
            }
            time++;
        }
        return time;
    }
}
