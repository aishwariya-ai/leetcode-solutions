class Solution {
    public static boolean isPalindrome(int x) {
        int temp=x;
        int rem,rev=0;
        if(x<0)
        {
            return false;
        }
        else
        {
        while(x!=0)
        {
            rem=x%10;
            rev=rev*10+rem;
            x=x/10;
        }
        if(temp==rev)
        {
            return true;
        }
        else
        {
            return false;
        }
        }
        
    }
    public static void main(String []args)
    {
        int n=121;
        if(isPalindrome(n))
        {
          System.out.println("True");
        }
        else
        {
           System.out.println("False"); 
        }
        
    }

}