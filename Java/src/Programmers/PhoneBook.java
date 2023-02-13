package Programmers;

import java.util.*;

public class PhoneBook {
    public boolean solution(String[] phone_book) {

        HashSet<String> phoneBook = new HashSet<>();

        for(String phoneNum : phone_book) {
            phoneBook.add(phoneNum);
        }

        for(String phoneNum : phone_book) {
            if(phoneNum.length() > 1) {
                StringBuilder subNum = new StringBuilder();

                for(int i=0; i<phoneNum.length()-1; i++) {
                    char cur = phoneNum.charAt(i);
                    subNum.append(cur);

                    if(phoneBook.contains(subNum.toString())) return false;
                }
            }
        }
        return true;
    }
}
