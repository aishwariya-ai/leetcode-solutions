class Solution {
    public static int getValue(char ch) {
        if (ch == 'I') return 1;
        else if (ch == 'V') return 5;
        else if (ch == 'X') return 10;
        else if (ch == 'L') return 50;
        else if (ch == 'C') return 100;
        else if (ch == 'D') return 500;
        else if (ch == 'M') return 1000;
        else return 0;
    }

    public static int romanToInt(String s) {
        int total = 0;

        for (int i = 0; i < s.length(); i++) {
            int current = getValue(s.charAt(i));
            if (i + 1 < s.length()) {
                int next = getValue(s.charAt(i + 1));

                if (current < next) {
                    total -= current; // subtract if smaller
                } else {
                    total += current; // otherwise add
                }
            } else {
                total += current; // add the last character
            }
        }

        return total;
    }

    public static void main(String[] args) {
        System.out.println(romanToInt("III"));      
        System.out.println(romanToInt("LVIII"));    
        System.out.println(romanToInt("MCMXCIV"));  
    }
}
