import java.util.LinkedList;
import java.util.Queue;
public class Insert {

    static class Node {
        int key;
        Node left, right;
        Node(int key) {
            this.key = key;
            left = null;
            right = null;
        }
    }

    static Node root;
    static Node temp = root;

    // 树的中序遍历
    static void inorder(Node temp) {
        if (temp == null) {
            return;
        }
        inorder(temp.left);
        System.out.print(temp.key + " ");
        inorder(temp.right);
    }

    static void insert(Node temp, int key) {
        
    }

}