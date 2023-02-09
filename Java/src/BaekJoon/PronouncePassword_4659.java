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
        bw.write(String.valueOf(passwords));
        bw.flush();
    }

    public String solution(List<String> passwords) {
        char[] vowels = { 'a', 'e', 'i', 'o', 'u'}; //모음
        for (String password : passwords)
            while(true){

                if(password.equals("end")) break;
                boolean acceptable = true;
                boolean hasVowel = false;
                int cntVowel = 0;//모음 카운트
                int cntConsonant = 0;//자음 카운트
                for(int i = 0; i < password.length(); i++){
                    char cur = password.charAt(i);
                    boolean isVoewl = false;
                    //모음인지 확인 : 모음이 연속 몇 번 나오는지 체크, 자음 연속 개수는 0으로
                    for(int j = 0; j < vowels.length; j++){
                        if(cur == vowels[j]){
                            isVoewl = true;
                            hasVowel = true;
                            cntVowel++;
                            cntConsonant = 0;
                            break;
                        }
                    }
                    //자음이라면
                    if(!isVoewl) {
                        cntConsonant++;
                        cntVowel = 0;
                    }
                    //문자열 끝까지 탐색했는데 모음이 없다면
                    if(i == password.length()-1){
                        if(!hasVowel) {
                            System.out.println("<" + password + "> is not acceptable.");
                            acceptable = false;
                            break;
                        }
                    }
                    if(i >= 1){
                        //동일한 문자가 2개 연속되는지 검사
                        if(cur == password.charAt(i-1) && cur != 'e' && cur != 'o'){
                            System.out.println("<" + password + "> is not acceptable.");
                            acceptable = false;
                            break;
                        }
                        //모음 혹은 자음이 3개 연속되는지 검사
                        else if(cntVowel >= 3 || cntConsonant >= 3){
                            System.out.println("<" + password + "> is not acceptable.");
                            acceptable = false;
                            break;
                        }
                    }
                }
                if(acceptable) System.out.println("<" + password + "> is acceptable.");
}
