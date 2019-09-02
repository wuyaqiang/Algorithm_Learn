
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linkedlist_merge_sort(head):
    '''
    归并排序
    '''
    def merge(h1, h2):
        sentinel = ListNode(0)
        cur = sentinel
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        cur.next = h1 if h1 else h2
        return sentinel.next

    if not head or not head.next:
        return head

    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    pre.next = None

    head_1 = linkedlist_merge_sort(head)
    head_2 = linkedlist_merge_sort(slow)
    return merge(head_1, head_2)

def linkedlist_quick_sort(head):
    '''
    快速排序
    '''
    def concat(left, mid, right):
        left_tail = get_tail(left)
        mid_tail = get_tail(mid)
        mid_tail.next = right
        if left_tail:
            left_tail.next = mid
            return left
        else:
            return mid

    def get_tail(head):
        if not head:
            return head
        while head.next:
            head = head.next
        return head

    if not head or not head.next:
        return head

    sentinel_left, sentinel_mid, sentinel_right = ListNode(0), ListNode(0), ListNode(0)
    left, mid, right = sentinel_left, sentinel_mid, sentinel_right
    pivot = head.val

    while head:
        if head.val < pivot:
            left.next = head
            left = left.next
        elif head.val == pivot:
            mid.next = head
            mid = mid.next
        else:
            right.next = head
            right = right.next
        head = head.next

    left.next, mid.next, right.next = None, None, None

    return concat(linkedlist_quick_sort(sentinel_left.next),
                  sentinel_mid.next,
                  linkedlist_quick_sort(sentinel_right.next))

def linkedlist_insert_sort(head):
    '''
    插入排序
    '''
    pass












