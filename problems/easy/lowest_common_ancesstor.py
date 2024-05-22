"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
 p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a
descendant of itself).”
"""
from problems.utils.TreeNode import TreeNode


def lca(root, p, q):
    """
    Idea is the root.val should be between p.val and q.val. Simple as that.
    So if root is greater than p and q, we move to left as it contains smaller values, as p and q are low
    if root is smaller than p and q, we move to right as right side contains higher values, as p and q are high
    :param root:
    :param p:
    :param q:
    :return:
    """
    print(root.val, p.val, q.val)
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
