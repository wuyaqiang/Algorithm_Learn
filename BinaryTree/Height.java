/*
* 求一个二叉树的深度.
*/
import java.util.LinkedList;
import java.util.Queue;

class Node {
    int val;
    Node left, right;
    public Node(int data) {
        val = data;
        left = null;
        right = null;
    }
}

class Height {
    public static void treeHeightRecursive(Node root) {
        if (root == null) {
            return 0;
        } else {
            int leftHeight = treeHeightRecursive(root.left);
            int rightHeight = treeHeightRecursive(root.right);

            if (leftHeight > rightHeight) {
                return (leftHeight + 1);
            } else {
                return (rightHeight + 1);
            }
        }
    }

    public static void treeHeightIterative(Node root) {
        if (root == null) {
            return 0;
        }
        Queue<Node> q = new LinkList();
        q.add(root);
        int height = 0;
        while (1) {
            int levelNodeCount = q.size();
            if (levelNodeCount == 0) {
                return height;
            }
            height++;
            while (levelNodeCount > 0) {
                Node curNode = q.peek();
                q.remove();
                if (curNode.left != null) {
                    q.add(curNode.left);
                }
                if (curNode.right != null) {
                    q.add(curNode.right);
                }
                levelNodeCount--;
            }
        }
    }

    public static void main(String[] args) {

    }
}

















