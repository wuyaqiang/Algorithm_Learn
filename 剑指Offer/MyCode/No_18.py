'''
剑指 Offer 第18题 及其变体
leetcode 237. Delete Node in a Linked List
leetcode 203. Remove Linked List Elements
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

def delete_duplicate_node(node):
    '''

    '''