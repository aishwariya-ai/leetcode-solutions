public class Solution {
    public static int lengthOfLastWord(String s) {
        s = s.trim();
        String[] words = s.split(" ");
        String lastWord = words[words.length - 1];
        return lastWord.length();
          }

    public static void main(String[] args) {
        String s = "Hello World";
        System.out.println(lengthOfLastWord(s));
    }
}
