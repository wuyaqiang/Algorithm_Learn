'''
剑指 Offer 第23题 链表有环问题
leetcode 141. Linked List Cycle
leetcode 142. Linked List Cycle II
'''

def has_cycle(head):
    '''
    判断链表是否有环
    leetcode 141. Linked List Cycle
    '''
    # 解法一：快慢指针
    # slow, fast = head, head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         return True
    # return False

    # 解法二：哈希表
    cur, exist = head, {}
    while cur:
        if cur in exist:
            return True
        exist[cur] = 1
        cur = cur.next
    return False


def find_cycle(head):
    '''
    找到链表中环的开始结点，如果链表没有环就返回None
    剑指 Offer 第23题
    leetcode 142. Linked List Cycle II
    '''
    has_cycle = False
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow











