"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.
"""

from problems.utils.TreeNode import TreeNode


def invert_binary_tree(root):
    """
    Idea is to do the breath first search and on processing every node, just swap the children of it.

    :param root:
    :return:
    """
    if root is None:
        return root
    queue = [root]
    while queue:
        temp = []
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            node.left, node.right = node.right, node.left
        queue = temp
    return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(4)
root.left.right.right = TreeNode(5)

invert_binary_tree(root)
