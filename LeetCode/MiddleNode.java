class ListNode {
    int val;
    ListNode next;
    ListNode (int x) {
        val = x;
    }
}

public class MiddleNode {
    public static ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode cur = head.next;
        while (cur != null) {
            length++;
            cur = cur.next;
        }
        int mid = (length / 2) + 1;
        for (int i = 0; i < mid; i++) {
            head = head.next;
        }
        return head;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(0);
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(3);
        head.next.next.next.next = new ListNode(4);
        head.next.next.next.next.next = new ListNode(5);
        ListNode middleNode = middleNode(head);
        for (ListNode node = middleNode; node != null; node = node.next) {
            System.out.println(node.val);
        }

    }
}