/** 
 * 二叉树的所有遍历方式：层序遍历、先序、中序、后序遍历
 * 包括他们的递归与非递归方式
 */
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;

class Node {
    int val;
    Node left, right;
    public Node(int data) {
        val = data;
        left = null;
        right = null;
    }
}

class Traversal {

    // 先序遍历(递归实现)：
    public static void preOrderRecursive(Node root) {
        if (root == null) {
            return ;
        }
        System.out.print(root.val + " ");
        preOrderRecursive(root.left);
        preOrderRecursive(root.right);
    }

    // 先序遍历(非递归实现), 一个栈：
    public static void preOrderIterative(Node root) {
        if (root == null) {
            return;
        }
        Stack<Node> nodeStack = new Stack<>();
        nodeStack.push(root);

        while (!nodeStack.isEmpty()) {
            Node currentNode = nodeStack.pop();
            System.out.print(currentNode.val + " ");
            if (currentNode.right != null) {
                nodeStack.push(currentNode.right);
            }
            if (currentNode.left != null) {
                nodeStack.push(currentNode.left);
            }
        }
    }

    // 中序遍历(递归实现)：
    public static void inOrderRecursive(Node root) {
        if (root == null) {
            return ;
        }
        inOrderRecursive(root.left);
        System.out.print(root.val + " ");
        inOrderRecursive(root.right);
    }

    // 中序遍历(非递归实现), 用栈
    public static void inOrderNonRecursive(Node root) {
        if (root == null) {
            return ;
        }
        Stack<Node> nodeStack = new Stack<Node>();
        Node curr = root;
        while (curr != null || nodeStack.size() > 0) {
            while (curr != null) {
                nodeStack.push(curr);
                curr = curr.left;
            }
            curr = nodeStack.pop();
            System.out.print(curr.val + " ");
            curr = curr.right;
        }
    }

    // 中序遍历(非递归实现), 不用栈
    // Morris算法, Time: O(n), Space: O(1)
    // 算法详情: http://www.learn4master.com/algorithms/morris-traversal-inorder-tree-traversal-without-recursion-and-without-stack
    public static void inOrderNonRecursiveNonStack(Node root) {
        Node cur = root;
        while (cur != null) {
            if (cur.left == null) {
                System.out.print(cur.val + " ");
                cur = cur.right;
            } else {
                Node pre = cur.left;
                while (pre.right != null && pre.right != cur) {
                    pre = pre.right;
                }
                if (pre.right == cur) {
                    pre.right = null;
                    System.out.print(cur.val + " ");
                    cur = cur.right;
                } else {
                    pre.right = cur;
                    cur = cur.left;
                }
            }
        }
    }

    // 后序遍历(递归实现)：
    public static void postOrderRecursive(Node root) {
        if (root == null) {
            return ;
        }
        postOrderRecursive(root.left);
        postOrderRecursive(root.right);
        System.out.print(root.val + " ");
    }

    // 后序遍历, 非递归, 两个栈
    public static void postOrderIterativeTwoStack(Node root) {
        if (root == null) {
            return;
        }
        Stack<Node> firstStack = new Stack<>();
        Stack<Node> secondStack = new Stack<>();
        firstStack.push(root);
        while (!firstStack.isEmpty()) {
            Node curNode = firstStack.pop();
            secondStack.push(curNode);
            if (curNode.left != null) {
                firstStack.push(curNode.left);
            }
            if (curNode.right != null) {
                firstStack.push(curNode.right);
            }
        }
        while (!secondStack.isEmpty()) {
            Node curNode = secondStack.pop();
            System.out.print(curNode.val + " ");
        }
    }

    // 后序遍历, 非递归, 一个栈
    public static void postOrderIterativeOneStack(Node root) {

    }

    // 层序遍历(递归实现)：
    public static void levelOrderRecursive(Node root) {

    }
    public void getGivenLevel(Node root, int level) {

    }

    // 层序遍历(队列实现)：
    public static void levelOrderQueue(Node root) {
        if (root == null) {
            return ;
        }
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node tempNode = queue.poll();
            System.out.print(tempNode.val + " ");

            if (tempNode.left != null) {
                queue.add(tempNode.left);
            }
            if (tempNode.right != null) {
                queue.add(tempNode.right);
            }
        }
    }

    // 按层螺旋遍历, 又称蛇形遍历, 递归实现
    public static void spiralOrderRecursive(Node root) {

    }

    // 按层螺旋遍历, 又称蛇形遍历, 迭代实现, 利用两个栈
    public static void spiralOrderIterative(Node root) {
        if (root == null) {
            return;
        }
        Stack<Node> currentLevel = new Stack<>();
        Stack<Node> nextLevel = new Stack<>();

        currentLevel.push(root);
        boolean leftToRight = true;

        while (!currentLevel.isEmpty()) {
            Node currentNode = currentLevel.pop();
            System.out.print(currentNode.val + " ");
            if (leftToRight) {
                if (currentNode.left != null) {
                    nextLevel.push(currentNode.left);
                }
                if (currentNode.right != null) {
                    nextLevel.push(currentNode.right);
                }
            } else {
                if (currentNode.right != null) {
                    nextLevel.push(currentNode.right);
                }
                if (currentNode.left != null) {
                    nextLevel.push(currentNode.left);
                }
            }
            
            if (currentLevel.isEmpty()) {
                leftToRight = !leftToRight;
                Stack<Node> temp = currentLevel;
                currentLevel = nextLevel;
                nextLevel = temp;
            }
        }
    }


    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        // System.out.println("\n先序遍历如下(递归)：");
        // preOrderRecursive(root);
        // System.out.println("\n先序遍历如下(非递归)：");
        // preOrderIterative(root);
        // System.out.println("\n中序遍历如下(递归)：");
        // inOrderRecursive(root);
        // System.out.println("\n中序遍历如下(非递归)：");
        // inOrderNonRecursive(root);
        // System.out.println("\n中序遍历如下(非递归非栈)：");
        // inOrderNonRecursiveNonStack(root);
        // System.out.println("\n后序遍历如下(递归)：");
        // postOrderRecursive(root);
        // System.out.println("\n后序遍历如下(非递归, 两个栈)：");
        // postOrderIterativeTwoStack(root);
        // System.out.println("\n层序遍历如下(递归)：");
        // levelOrderRecursive(root);
        // System.out.println("\n层序遍历如下(队列)：");
        // levelOrderQueue(root);
        // System.out.println("\n蛇形遍历如下(两个栈)：");
        // spiralOrderIterative(root);
    }
}