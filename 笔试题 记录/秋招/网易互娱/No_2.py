#coding=utf-8
import sys

class Node(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def func(root):
    if not root:
        return "NO"

    cur_level_sum, cur_level = -1, [root]

    while cur_level:
        cur_level_val = []
        next_level = []

        for node in cur_level:
            cur_level_val.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if cur_level_sum >= sum(cur_level_val):
            return "NO"

        cur_level_sum = sum(cur_level_val)
        cur_level = next_level

    return "YES"

if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())

    for _ in range(T):

        N = int(sys.stdin.readline().strip())
        id_node_dict = {}

        # 构建哈希表 key： 结点编号  value：结点
        for i in range(N):
            val, left, right = list(map(int, sys.stdin.readline().strip().split()))
            id_node_dict[i] = Node(val, left, right)

        # 确定根节点：
        sub_tree_id = []
        for id, node in id_node_dict.items():
            if node.left != -1 and node.left not in sub_tree_id:
                sub_tree_id.append(node.left)
            if node.right != -1 and node.right not in sub_tree_id:
                sub_tree_id.append(node.right)
        root_id = sum(range(N)) - sum(sub_tree_id)

        # 构建二叉树：
        for id, node in id_node_dict.items():
            if node.left == -1:
                node.left = None
            else:
                node.left = id_node_dict[node.left]
            if node.right == -1:
                node.right = None
            else:
                node.right = id_node_dict[node.right]

        print(func(id_node_dict[root_id]))












