import java.util.Scanner;

class SearchElement{
    public static void main(String[] args){
        SearchElement a = new SearchElement();
        Scanner scan = new Scanner(System.in);
        int demo_array[] = {12,34,10,6,40};
        System.out.println("Enter the key you want search: ");
        int key = scan.nextInt();
        int position = a.Search(demo_array,key);
        if(position == -1){
            System.out.println("the key " + key + " is not in array.");
        }
        else{
            System.out.println("the key " + key + " is at " + position + " of array.");
        }
    }
    int Search(int arr[],int key){
        int n = arr.length;
        int i;
        for(i = 0; i < n; i++){
            if(arr[i] == key){
                break;
            }
        }
        if(i == n){
            return -1;
        }
        else{
            return i;
        }
    }
}