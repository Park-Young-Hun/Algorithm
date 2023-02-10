package BaekJoon;

import java.io.*;
import java.util.*;

public class PronouncePassword_4659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        List<String> passwords = new ArrayList<>();

        while (true) {
            String password = br.readLine();

            if (password.equals("end")) {
                break;
            }
            passwords.add(password);
        }

        for (String password : passwords) {
            String answer = solution(password);
            bw.write("<" + password + ">" + " is " + answer + "\n");
        }
        bw.flush();
    }

    public static String solution(String password) {
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};

        boolean hasVowel = false;
        boolean isSameLetter = false;

        int vowelCnt = 0;
        int consonantCnt = 0;

        String answer = "acceptable.";

        for (int i=0; i<password.length(); i++) {
            boolean isVowel = false;
            char letter = password.charAt(i);

            if (i>0) {
                if (letter == password.charAt(i-1) && letter != 'e' && letter != 'o') {
                    isSameLetter = true;
                    break;
                }
            }

            for (char vowel : vowels) {
                if (letter == vowel) {
                    hasVowel = true;
                    isVowel = true;
                    vowelCnt ++;
                    consonantCnt = 0;
                    break;
                }
            }

            if (!isVowel) {
                vowelCnt = 0;
                consonantCnt ++;
            }

            if (vowelCnt > 2 || consonantCnt > 2) break;
        }
        if (!hasVowel || vowelCnt > 2 || consonantCnt > 2 || isSameLetter) {
            answer = "not " + answer;
        }

        return answer;
    }
}
