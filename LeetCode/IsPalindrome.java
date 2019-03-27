class IsPalindrome {
    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int reverseNum = 0;
        int copyX = x;
        while (copyX != 0) {
            reverseNum = reverseNum * 10 + copyX % 10;
            copyX /= 10;
        }
        return (reverseNum == x);
    }
    public static void main(String[] args) {
        int x = 121;
        int reverseNum = isPalindrome(x);
        System.out.println(reverseNum);
    }
}