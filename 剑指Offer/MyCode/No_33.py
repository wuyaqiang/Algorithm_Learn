'''
判断一个数组是否为某一个二叉搜索树的后序遍历结果
剑指 Offer 第33题 及其变体
leetcode 255  Verify Preorder Sequence in Binary Search Tree
'''

def verify_BST_postorder_sequence(seq):

    if not seq or len(seq) < 1:
        return False
    length = len(seq)
    root = seq[length - 1]
    i = 0
    while i < length - 1 and seq[i] < root:
        i += 1
    j = i
    while j < length - 1:
        if seq[j] < root:
            return False
        j += 1
    left, right = True, True
    if i > 0:
        left = verify_BST_postorder_sequence(seq[ : i])
    if j < length - 1:
        right = verify_BST_postorder_sequence(seq[i : length - 1])

    return left and right

if __name__ == '__main__':

    print(verify_BST_postorder_sequence([7,4,6,5]))

