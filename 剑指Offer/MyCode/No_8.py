'''
剑指 Offer 第8题 二叉树的下一个结点
'''

def get_next_node(node):
    '''
    给定一颗二叉树和其中一个结点，请找出中序遍历序列的下一个结点;
    树中包含指向左右孩子的指针与指向父结点的指针;
    该题分为三种情况：
    1. 如果一个结点有右子树，则它的下一个结点就是它右子树中的最左子结点
    2. 如果一个结点没有右子树，且它是它父结点的左子结点，则它的下一个结点就是它的父结点
    3. 如果一个结点没有右子树，且它是它父结点的右子结点，我们可以沿着指向父结点的指针一直向上遍历，
       直到找到一个是它父结点的左子结点的结点，则这个结点的父结点就是要找的下一个结点
    '''
    if not node:
        return None
    next_node = None
    if node.right:
        next_node = node.right
        while next_node.left:
            next_node = next_node.left
    else:
        cur = node
        cur_parent = node.parent
        while cur_parent and cur == cur_parent.right:
            cur = cur_parent
            cur_parent = cur_parent.parent
        next_node = cur_parent
    return next_node



