import java.util.Scanner;

class ArrayRotation2{
    public static void main(String[] args){
        ArrayRotation a = new ArrayRotation();
        Scanner scan = new Scanner(System.in);
        int[] demo_array = new int[10];
        System.out.println("Enter the array: ");
        for(int i = 0; i < 10; i++){
            demo_array[i] = scan.nextInt();
        }
        System.out.println("Enter the d: ");
        int d = scan.nextInt();
        a.Reverse(demo_array,0,d-1);
        a.Reverse(demo_array,d,demo_array.length-1);
        a.Reverse(demo_array,0,demo_array.length-1);
        for(int i = 0; i < demo_array.length; i++){
            System.out.print(demo_array[i] + " ");
        }
    }
    void Reverse(int arr[],int start,int end){
        int temp;
        while(start < end){
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}