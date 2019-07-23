'''
剑指 Offer 第37题
leetcode 297. Serialize and Deserialize Binary Tree
leetcode 449. Serialize and Deserialize BST
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SD_BT:
    '''
    二叉树的序列化和反序列化
    '''
    def serialize(self, root):
        def helper(node):
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
        res = []
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper():
            node_val = next(val_list)
            if node_val == "#":
                return None
            else:
                node = TreeNode(int(node_val))
                node.left = helper()
                node.right = helper()
                return node

        val_list = iter(data.split(","))
        return helper()


class SD_BST:
    '''
    二叉搜索树的序列化和反序列化
    '''
    def serialize(self, root):


    def deserialize(self, data):
        pass






















