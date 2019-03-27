//java program to print inorder traversal without recursive and without stack

class Node{
    int data;
    Node left,right;
    public Node(int item){
        data = item;
        left = right = null;
    }
}

class MorrisTraversal{
    Node root;
    void morrisTraversal(Node root){
        Node current,pre;
        if(root == null)
            return;
        current = root;
        while(current != null){
            
        }
    }
}