import java.util.HashMap;
import java.util.ArrayList;


public class MaratonLoser {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> participant_map = new HashMap<>();
        HashMap<String, Integer> winners_map = new HashMap<>();

        for (String str : participant) {
            if (participant_map.containsKey(str)) {
                participant_map.put(str, participant_map.get(str) + 1);
            }
            else {
                participant_map.put(str, 1);
            }
        }

        for (String str : completion) {
            participant_map.put(str, participant_map.get(str) - 1);

        }

        ArrayList<String> keyList = new ArrayList<>(participant_map.keySet());
        for(String key : keyList) {
            if(participant_map.get(key) == 1) {
                answer = key;
            }
        }

        return answer;
    }
}
