'''
剑指 Offer 第7题 重建二叉树 及其变体
leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree_1(preorder, inorder):
    '''
    leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
    '''
    if not preorder or not inorder or len(preorder) == 0 or len(inorder) == 0:
        return None

    root_val = preorder[0]
    inorder_root_idx = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = build_tree_1(preorder[1: 1 + inorder_root_idx], inorder[: inorder_root_idx])
    root.right = build_tree_1(preorder[1 + inorder_root_idx:], inorder[inorder_root_idx + 1:])

    return root

def build_tree_2(inorder, postorder):
    '''
    leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
    '''
    if not inorder or not postorder or len(inorder) == 0 or len(postorder) == 0:
        return None

    root_val = postorder[-1]
    inorder_root_idx = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = build_tree_2(inorder[: inorder_root_idx], postorder[: inorder_root_idx])
    root.right = build_tree_2(inorder[inorder_root_idx + 1:], postorder[inorder_root_idx: -1])

    return root


















