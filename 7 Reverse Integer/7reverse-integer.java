class Solution {
    public static int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int rem = x % 10;

            // Check for overflow BEFORE updating rev
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && rem > 7)) {
                return 0; // Overflow
            }
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && rem < -8)) {
                return 0; // Underflow
            }

            rev = rev * 10 + rem;
            x = x / 10;
        }

        return rev;
    }

    public static void main(String args[]) {
        int x = -2147483412;
        int total = reverse(x);
        System.out.println(total);
    }
}
