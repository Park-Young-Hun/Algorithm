package BaekJoon;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.StringTokenizer;

public class PronouncePassword_4659 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //StringTokenizer st = new StringTokenizer(br.readLine());

        List<String> passwords = new ArrayList<>();

        while (true) {
            String password = br.readLine();

            if (password.equals("end")) {
                break;
            }
            passwords.add(password);
        }
        bw.write(String.valueOf(passwords));
        bw.flush();
    }

    public String solution(List<String> passwords) {
        String[] vowel = {"a", "e", "o", "i", "u"};

        for (String password : passwords) {

        }
    }
}
