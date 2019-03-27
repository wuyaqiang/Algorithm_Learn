class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}

public class AddTwoNumbers2 {
    public static ListNode addTwoNumbers2(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        int sum = 0;
        ListNode sentinel = new ListNode(1);
        ListNode cur = sentinel;
        while (!s1.empty() || !s2.empty()) {
            if (!s1.empty()) {
                sum = sum + s1.pop();
            }
            if (!s2.empty()) {
                sum = sum + s2.pop();
            }
            ListNode newNode = new ListNode(sum % 10);
            newNode.next = sentinel.next;
            sentinel.next = newNode;
            sum /= 10;
        }
        return sum != 0? sentinel : sentinel.next;
    }
}