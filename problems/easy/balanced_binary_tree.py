"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree
in which the depth of the two subtrees of every node never differs by more than one.
"""
from problems.utils.TreeNode import TreeNode


def height(root):
    if not root:
        return 0

    left = height(root.left)
    right = height(root.right)

    return max(left, right) + 1


def height_balanced(root):
    if not root:
        return 0

    left = height(root.left)
    right = height(root.right)
    print(left, right)

    if abs(left - right) > 1:
        raise Exception("Tree not balanced")

    return max(left, right) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(4)
root.left.right.right = TreeNode(5)

print(height(root))
# print(height_balanced(root))

try:
    height_balanced(root)
    print("Tree Balanced")
except Exception as e:
    print(e)
    print("Tree not Balanced")
