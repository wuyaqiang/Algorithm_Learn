'''
剑指 Offer 第6题 从尾到头打印链表
'''

def print_list_reversed(head):

    # 解法一：用栈
    # stack = []
    # while head:
    #     stack.append(head)
    # while stack:
    #     print(stack.pop().val)

    # 解法二：递归
    if not head:
        return
    if head.next:
        print_list_reversed(head.next)
    print(head.val)

