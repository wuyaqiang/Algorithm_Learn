class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}

public class AddTwoNumbers {
    /* 下面解法错误：此题不能直接将两数相加，会存在整形溢出问题，long整形都会溢出
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long num1 = 0, num2 = 0;
        int i = 0;
        for (ListNode node = l1; node != null; node = node.next) {
            num1 = num1 + node.val * (long) Math.pow(10, i);
            i++;
        }
        int j = 0;
        for (ListNode node = l2; node != null; node = node.next) {
            num2 = num2 + node.val * (long) Math.pow(10, j);
            j++;
        }
        long sum = num1 + num2;
        ListNode firstNode = new ListNode(0);
        ListNode tailNode = firstNode;
        while (sum != 0) {
            long currentNum = sum % 10;
            ListNode oldTailNode = tailNode;
            ListNode currentNode = new ListNode((int)currentNum);
            oldTailNode.next = currentNode;
            tailNode = currentNode;
            sum = sum / 10;
        }
        if (firstNode.next != null) {
            return firstNode.next;
        } else {
            return firstNode;
        }
    }
    */
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        /* 所以不能采用两个数直接相加，然后将得到的和转换成链表的算法，要将链表中的每个结点单独相加，
        直接一个数一个数生成和的链表 */
        ListNode sentinel = new ListNode(0);
        ListNode cur = sentinel;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sum = (l1 == null? 0 : l1.val) + (l2 == null? 0 : l2.val) + carry;
            ListNode newNode = new ListNode(sum % 10);
            cur.next = newNode;
            cur = newNode;
            carry = sum / 10;
            l1 = (l1 == null? l1 : l1.next);
            l2 = (l2 == null? l2 : l2.next);
        }
        return sentinel.next;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(9);
        // l1.next = new ListNode(4);
        // l1.next.next = new ListNode(3);
        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        ListNode sum = addTwoNumbers(l1, l2);
        for (ListNode node = sum; node != null; node = node.next) {
            System.out.println(node.val);
        }
    }
}