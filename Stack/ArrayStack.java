class ArrayStack{
    static final int MAX = 100;
    int top;
    int stack_array[] = new int[MAX];

    boolean isEmpty(){
        return (top < 0);
    }

    boolean Push(int x){
        if(top >= MAX){
            System.out.println("Stack Overflow!");
            return false;
        }
        else{
            stack_array[++top] = x;
            return true;
        }
    }

    int Pop(){
        if(top < 0){
            System.out.println("Stack Underflow!");
            return 0;
        }
        else{
            int x = stack_array[top--];
            return x;
        }
    }
}
class Main{
    public static void main(String args[]){
        ArrayStack s = new ArrayStack();
        s.Push(10);
        s.Push(20);
        s.Push(30);
        System.out.println(s.Pop() + "poped from stack.");
    }
}