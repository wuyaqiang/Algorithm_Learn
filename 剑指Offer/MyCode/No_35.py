'''
剑指 Offer 第35题 复杂链表的复制
leetcode 138. Copy List with Random Pointer
'''

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):

    # 解法一：利用哈希表
    # copy_dict = {}
    # cur = head
    # while cur:
    #     copy_dict[cur] = Node(cur.val)
    #     cur = cur.next
    # cur = head
    # while cur:
    #     copy_dict[cur].next = copy_dict[cur.next]
    #     copy_dict[cur].random = copy_dict[cur.random]
    #     cur = cur.next
    # return copy_dict[head]

    # 解法二：直接在原始链表中操作
    cur = head
    while cur:  # 第一轮遍历，复制链表结点，链表长度变为两倍
        next_node = cur.next
        copy_node = Node(cur.val)
        cur.next = copy_node
        copy_node.next = next_node
        cur = next_node
    cur = head
    while cur:  # 第二轮遍历，给复制结点指定random指针指向
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur = head
    sentinel = Node(0)
    copy_cur = sentinel
    while cur:  # 第三轮遍历，提取出所有复制结点
        next_node = cur.next.next
        copy_node = cur.next

        copy_cur.next = copy_node
        copy_cur = copy_node

        cur.next = next_node
        cur = next_node
    return sentinel.next

















