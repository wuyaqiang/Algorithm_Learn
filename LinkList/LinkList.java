public class LinkList<Item>{

    private class Node{
        Item data;
        Node next;
    }
    private Node first;
    private int size;

    public boolean isEmpty(){
        return size == 0;
    }

    public int size(){
        return size;
    }

    public void insertHead(Item data){
        Node old_first = first;
        first = new Node();
        first.data = data;
        first.next = old_first;
    }

    public void deleteHead(){
        first = first.next;
    }

    public void insertTail(Item data){
        if (isEmpty()) {
            first = new Node();
            first.data = data;
        } else {
            Node current;
            for(current = first; current.next != null; current = current.next );

            Node new_node = new Node();
            new_node.data = data;
            current.next = new_node;
        }
        size++;
    }

    public void deleteTail() {
        if (!isEmpty()) {
            if (size == 1) {
                first = null;
            } else {
                Node current = first;
                for(int i = 0; i < size - 2; i++) {
                    current = current.next;
                }
                current.next = null;
            }

            size--;
        }
    }

    public void deleteK(int k) {
        // 删除第k个结点
        if (isEmpty() || k > size) {
            return;
        }
        if (k == 1) {
            first = first.next;
        } else {
            Node current;
            int count = 1;
            for (current = first; current != null; current = current.next) {
                if (count == k - 1 && current.next != null) {
                    current.next = current.next.next;
                    break;
                }
                count++;
            }
        }

        size--;
    }

    public boolean find(String key) {
        if (isEmpty()) {
            return false;
        }
        boolean is_find = false;
        for (Node current = first; current != null; current = current.next) {
            if (current.data.equals(key)) {
                is_find = true;
                break;
            }
        }
        return is_find;
    }

    public void remove(String key) {
        // 删除链表中所有data值为key的结点
        if (isEmpty() || key == null) {
            return;
        }

        while (first != null && first.data.equals(key)) {
            first = first.next;
            size--;
        }

        Node pre_node;
        for (pre_node = first; pre_node.next != null; pre_node = pre_node.next) {
            if (pre_node.next.data.equals(key)) {
                pre_node.next = pre_node.next.next;
                size--;
            }
        }
    }

    public Node reverseIterative(Node first) {
        // （迭代方式）将链表反转，返回结果链表的首结点
        Node reverse = null;
        while (first != null) {
            Node second = first.next;
            first.next = reverse;
            reverse = first;
            first = second;
        }
        return reverse;
    }
    public Node reverseRecursive(Node first) {
        // （递归方式）将链表反转，返回结果链表的首结点
        if (first == null) return null;
        if (first.next == null) return first;
        Node second = first.next;
        Node rest = reverseRecursive(second);
        second.next = first;
        first.next = null;
        return rest;
    }

}









































































