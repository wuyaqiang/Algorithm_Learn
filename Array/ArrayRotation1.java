import java.util.Scanner;

class ArrayRotation1{
    public static void main(String[] args){
        ArrayRotation a = new ArrayRotation();
        int[] demo_array = new int[10];
        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter the array: ");
        for(int i = 0;i < 10;i++){
            demo_array[i] = scan.nextInt();
        }
        System.out.println("Please enter the d: ");
        int d = scan.nextInt();
        a.Rotate(demo_array,d);
        a.PrintArray(demo_array);
    }
    void Rotate(int arr[],int d){
        int temp;
        for(int i = 0; i < d; i++){
            temp = arr[0];
            for(int j = 0; j < arr.length - 1; j++){
                arr[j] = arr[j+1];
            }
            arr[arr.length-1] = temp;
        }
    }
    void PrintArray(int arr[]){
        for(int i = 0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
