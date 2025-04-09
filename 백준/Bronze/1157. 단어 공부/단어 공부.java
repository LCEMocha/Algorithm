import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next().toUpperCase();
        sc.close();

        int[] alphabet = new int[26];

        for (int i=0; i < input.length(); i++) {
            alphabet[input.charAt(i) - 'A']++;
        }

        int max = -1;
        char result = '?';

        for (int j=0; j<26; j++) {
            if (alphabet[j] > max) {
                max = alphabet[j];
                result = (char)(j + 'A');
            } else if (alphabet[j] == max) {
                result = '?';
            }
        }
        System.out.println(result);
    }
}