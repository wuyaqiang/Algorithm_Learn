'''
二叉树的遍历(所有方法)
剑指 Offer 第32题 及其变体
1. 前序(递归、非递归)
2. 中序(递归、非递归、Morris算法)
3. 后序(递归、非递归)
4. 层序(不分行打印、分行打印、zigzag遍历)
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_recursive(root):
    '''
    前序遍历 递归
    '''
    def helper(root):
        if not root:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    res = []
    helper(root)
    return res

def pre_order_iterative(root):
    '''
    前序遍历 非递归 一个栈
    '''
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res

def in_order_recursive(root):
    '''
    中序遍历 递归
    '''
    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    res = []
    helper(root)
    return res

def in_order_iterative(root):
    '''
    中序遍历 非递归 一个栈
    '''
    if not root:
        return []
    res, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

def in_order_morris(root):
    '''
    中序遍历 非递归 不用栈 ——> Morris算法
    http://www.learn4master.com/algorithms/morris-traversal-inorder-tree-traversal-without-recursion-and-without-stack
    '''
    res = []
    cur = root
    while cur:
        if not cur.left:
            res.append(cur.val) # if there is no left child, visit current node
            cur = cur.right # then we go the right branch
        else:
            # find the right most leaf of root.left node.
            pre = cur.left
            # when pre.right == null, it means we go to the right most leaf
            # when pre.right == cur, it means the right most leaf has been visited in the last round
            while pre.right and pre.right != cur:
                pre = pre.right
            # this means the pre.right has been set, it's time to go to current node
            if pre.right == cur:
                pre.right = None
                # means the current node is pointed by left right most child
                # the left branch has been visited, it's time to print the current node
                res.append(cur.val)
                cur = cur.right
            else:
                # the fist time to visit the pre node, make its right child point to current node
                pre.right = cur
                cur = cur.left
    return res

def post_order_recursive(root):
    '''
    后序遍历 递归
    '''
    def helper(root):
        if not root:
            return
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    res = []
    helper(root)
    return res

def post_order_iterative(root):
    '''
    后序遍历 非递归 一个栈
    '''
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        cur = stack.pop()
        res.insert(0, cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res

def level_order(root):
    '''
    层序遍历 非递归 一个队列 不按行打印
    '''
    if not root:
        return []
    res, queue = [], [root]
    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res

def level_order_by_row(root):
    '''
    层序遍历 非递归 一个队列 按行打印
    '''
    if not root:
        return []
    res, cur_level = [], [root]
    while cur_level:
        cur_level_val = []
        next_level = []
        for node in cur_level:
            cur_level_val.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res.append(cur_level_val)
        cur_level = next_level
    return res

def level_order_zigzag(root):
    '''
    层序遍历 非递归 按 ZigZag 顺序遍历
    与层序遍历按行打印类似，只是加了一个 left_to_right 标志
    '''
    if not root:
        return []
    res, cur_level = [], [root]
    left_to_right = True
    while cur_level:
        cur_level_val, next_level = [], []
        for node in cur_level:
            if left_to_right:
                cur_level_val.append(node.val)
            else:
                cur_level_val.insert(0, node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res.append(cur_level_val)
        cur_level = next_level
        left_to_right = not left_to_right

    return res


if __name__ == '__main__':

    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)

    # print(pre_order_recursive(root))
    # print(pre_order_iterative(root))

    print(in_order_recursive(root))
    print(in_order_iterative(root))
    print(in_order_morris(root))

    # print(post_order_recursive(root))
    # print(post_order_iterative(root))

    # print(level_order(root))
    # print(level_order_by_row(root))
    # print(level_order_zigzag(root))











