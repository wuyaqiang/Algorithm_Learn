/**
 * 快速排序算法
 */

public class QuickSort {
    public static void sort(int[] arr, int l, int r) {
        if (l < r) {
            int i = l, j = r;
            int axis = arr[l];
            while (i < j) {
                while (i < j && arr[j] >= axis) j--;
                if (i < j) arr[i++] = arr[j];

                while (i < j && arr[i] < axis) i++;
                if (i < j) arr[j--] = arr[i];
            }

            arr[i] = axis;
            sort(arr, l, i - 1);
            sort(arr, i + 1, r);
        }
    }

    public static void main(String[] args) {
        int[] arr = {3,1,5,2,4,9,0};
        sort(arr, 0, arr.length - 1);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

}