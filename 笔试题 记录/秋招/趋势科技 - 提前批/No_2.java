import java.util.Scanner;

public class Main {
    private static String process(String num1, String num2)
    {

        String[] string_nums = num1.split();
        int[] nums = new int[string_nums.length];
        for (int i = 0; i < string_nums.length; i++) {
            nums[i] = Integer.parseInt(string_nums[i]);
        }
        int res = 0;
        int[] a = {1, 5, 10, 20, 50, 100};

        for (int i = 0; i <= nums[5]; i++) {
            for (int j = 0; j <= nums[4]; j++) {
                for (int k = 0; k <= nums[3]; k++) {
                    for (int l = 0; l <= nums[2]; l++) {
                        for (int m = 0; m <= nums[1]; m++) {
                            int n = Integer.parseInt(num2) - (i * a[5] + j * a[4] + k * a[3] + l * a[2] + m * a[1]);
                            if (n <= nums[0] && n > 0) {
                                res += n + i + j + k + l + m;
                            }
                        }
                    }
                }
            }
        }
        if (res <= 0) {
            res = -1;
        }
        return res;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String strValueSequences = sc.nextLine();
        String strChargeNum = sc.nextLine();

        String sum = process(strValueSequences, strChargeNum);
        System.out.println(sum);
    }