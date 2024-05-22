"""
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root. The length of a path between two nodes is
represented by the number of edges between them.

This is definitely not a easy problem, it is a medium problem at least
"""

from problems.utils.TreeNode import TreeNode


def diameter_of_a_tree(root, ans):
    """
    This is a modification of finding the height of the tree.
    So for every node we need to calculate the height/depth on both the sides of the node and sum it
    The maximum sum is the answer here.

    :param root:
    :param ans:
    :return:
    """
    if not root:
        return [0, ans]

    left, ans = diameter_of_a_tree(root.left, ans)
    right, ans = diameter_of_a_tree(root.right, ans)

    ans = max(left + right, ans)
    return [max(left, right) + 1, ans]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(4)
root.left.right.right = TreeNode(5)

print(diameter_of_a_tree(root, 0)[1])
