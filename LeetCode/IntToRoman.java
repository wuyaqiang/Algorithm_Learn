class IntToRoman {
    puclic String intToRoman(int num) {
        int[] value = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder romanStr = new StringBuilder();
        int temp = 0;
        for (int i = 0; i < value.length; i++) {
            while ((temp + value[i]) <= num) {
                romanStr.append(roman[i]);
                temp += value[i];
            }
        }
        String str = romanStr.toString();
        return str;
    }
}