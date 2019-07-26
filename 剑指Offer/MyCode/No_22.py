'''
剑指 Offer 第22题 链表中倒数第k个结点
leetcode 19. Remove Nth Node From End of List
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_from_end(head, n):
    # 本题要考虑 n 小于 1 和 n 大于链表长度两种情况
    if not head or n < 1:
        return head
    sentinel = ListNode(0)
    sentinel.next = head
    slow, fast = sentinel, sentinel
    for _ in range(n):
        if not fast:    # 防止 n 大于链表长度
            return None
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return sentinel.next


