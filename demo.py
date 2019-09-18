#coding=utf-8
import sys

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(node_values, i, n):

    if i >= n or node_values[i] == "null":
        return None

    root = TreeNode(node_values[i])
    root.left = build_tree(node_values, 2 * i + 1, n)
    root.right = build_tree(node_values, 2 * i + 2, n)
    return root

def preorder_traverse(root):

    def traverse(root):
        if not root:
            return
        res.append(root.val)
        traverse(root.left)
        traverse(root.right)
    res = []
    traverse(root)
    return res

def node_sum(preorder, compute_values):

    res = 0
    for i in compute_values:
        res += int(preorder[i])

    return res


if __name__ == "__main__":

    node_values = list(sys.stdin.readline().strip().split(","))

    node_values = [i.strip() for i in node_values]

    compute_values = list(map(int, sys.stdin.readline().strip().split(",")))

    root = build_tree(node_values, 0, len(node_values))
    preorder_list = preorder_traverse(root)
    print(preorder_list)
    res = node_sum(preorder_list, compute_values)

    print(res)
