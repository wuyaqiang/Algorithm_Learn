'''
剑指 Offer 第54题
同 leetcode 230. Kth Smallest Element in a BST
'''

def kthSmallest(root, k):
    if not root or k < 1:
        return -1
    count = 0
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        count += 1
        if count == k:
            return cur.val
        cur = cur.right
    return -1