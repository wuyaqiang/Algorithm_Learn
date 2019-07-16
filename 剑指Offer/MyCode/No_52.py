'''
剑指 Offer 第52题 及其变体
同 leetcode 160. Intersection of Two Linked Lists
'''

def first_common_node(headA, headB):
    '''
    两个链表的第一个公共结点
    '''
    # 解法一：先求出两个链表长度
    # lenA, lenB = 0, 0
    # curA, curB = headA, headB
    # while curA:
    #     lenA += 1
    #     curA = curA.next
    # while curB:
    #     lenB += 1
    #     curB = curB.next
    # curA, curB = headA, headB
    # while lenA > lenB:
    #     curA = curA.next
    #     lenA -= 1
    # while lenA < lenB:
    #     curB = curB.next
    #     lenB -= 1
    # while curA != curB:
    #     curA = curA.next
    #     curB = curB.next
    # return curA

    # 解法二：不求长度
    if not headA or not headB:
        return None
    curA, curB = headA, headB
    while curA != curB:
        curA = headB if curA == None else curA.next
        curB = headA if curB == None else curB.next
    return curA