'''
剑指 Offer 第25题 合并两个排序的链表
leetcode 101. Symmetric Tree
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):

    # # 解法一：递归
    # if not l1:
    #         return l2
    # if not l2:
    #     return l1
    # if l1.val <= l2.val:
    #     l1.next = mergeTwoLists(l1.next, l2)
    #     return l1
    # else:
    #     l2.next = mergeTwoLists(l1, l2.next)
    #     return l2

    # 解法二：非递归
    sentinel = ListNode(0)
    cur = sentinel
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return sentinel.next