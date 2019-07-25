'''
剑指 Offer 第24题 链表反转
leetcode 206. Reverse Linked List
leetcode 92. Reverse Linked List II
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(head):
    '''
    剑指 Offer 第24题 链表反转
    leetcode 206. Reverse Linked List
    '''
    # 解法一：头插法
    new_head = None
    while head:
        next_node = head.next
        head.next = new_head
        new_head = head
        head = next_node
    return new_head

    # 解法二：原地逆置
    # pre, cur = None, head
    # while cur:
    #     next_node = cur.next
    #     cur.next = pre
    #     pre = cur
    #     cur = next_node
    # return pre

    # 解法三：递归
    # def helper(cur, pre):
    #     if not cur:
    #         return pre
    #     next_node = cur.next
    #     cur.next = pre
    #     return helper(next_node, cur)
    # return helper(head, None)

def reverse_list_between(head, m, n):
    '''
    反转链表中位置 m 到 n 的部分
    leetcode 92. Reverse Linked List II
    '''
    if not head:
        return None
    sentinel = ListNode(0)
    sentinel.next = head

    before = sentinel   # 指向第 m-1 个结点
    for _ in range(m - 1):
        before = before.next

    first = before.next     # 指向第 m 个结点，即逆置后的第 n 个结点

    cur, pre = first, None
    for _ in range(n - m + 1):
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node

    # 将逆置之后的链表，链接到原始链表中：
    before.next = pre   # pre 此时指向原始链表的第 n 个结点，即逆置之后的第 m 个结点
    first.next = cur    # cur 此时指向原始链表的第 n+1 个结点，需要链接在 first 结点之后

    return sentinel.next














