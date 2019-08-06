'''
剑指 Offer 第18题 及其变体
leetcode 237. Delete Node in a Linked List
leetcode 203. Remove Linked List Elements
leetcode 83. Remove Duplicates from Sorted List
leetcode 82. Remove Duplicates from Sorted List II
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(node):
    """
    剑指 Offer 第18题 及其变体
    leetcode 237. Delete Node in a Linked List
    """
    node.val = node.next.val
    node.next = node.next.next

def remove_elements(head, val):
    '''
    leetcode 203. Remove Linked List Elements
    '''
    sentinel = ListNode(0)
    sentinel.next = head
    cur = sentinel
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
            continue
        cur = cur.next
    return sentinel.next

def delete_duplicate_node_1(head):
    '''
    leetcode 83. Remove Duplicates from Sorted List
    '''
    if not head:
        return head
    cur = head
    while cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
            continue
        cur = cur.next
    return head


def delete_duplicate_node_2(head):
    '''
    leetcode 82. Remove Duplicates from Sorted List II
    '''
    sentinel = ListNode(0)
    sentinel.next = head
    pre, cur = sentinel, head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        if pre.next == cur:
            pre = pre.next
        else:
            pre.next = cur.next
        cur = cur.next
    return sentinel.next















