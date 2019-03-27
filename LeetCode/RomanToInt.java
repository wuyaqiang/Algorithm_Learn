// HashMap解法
class RomanToInt {
    public int romanToInt(string s) {
        if ( s == null || s.length() == 0) {
            return -1;
        }
        HashMap<Character, Integer> map = new HashMap<Charater, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int len = s.length();
        int result = 0;
        for (int i = 0; i < len - 1; i++) {
            if (map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {
                result -= map.get(s.charAt(i));
            } else {
                result += map.get(s.charAt(i));
            }
        }
        result += map.get(s.charAt(len - 1));
        return result;
    }
}

/* 
// 简单解法
class RomanToInt {
    public int romanToInt(String s) {
        len = s.length();
        int[] nums = new int[len];
        for (int i = 0; i < len; i++) {
            switch (s.charAt(i)) {
                case 'M':
                    nums[i] = 1000;
                    break;
                case 'D':
                    nums[i] = 500;
                    break;
                case 'C':
                    nums[i] = 100;
                    break;
                case 'L':
                    nums[i] = 50;
                    break;
                case 'X':
                    nums[i] = 10;
                    break;
                case 'V':
                    nums[i] = 5;
                    break;
                case 'I':
                    nums[i] = 1;
                    break;
            }
        }
        sum = 0;
        for (int i = 0; i < len - 1; i++) {
            if (nums[i] < nums[i+1]) {
                sum -= nums[i];
            }
            else {
                sum += nums[i];
            }
        }
        sum += nums[len - 1];
        return sum;
    }
}

*/