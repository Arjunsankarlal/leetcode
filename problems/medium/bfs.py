"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree,
 return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from problems.utils.TreeNode import TreeNode


def bfs(root: TreeNode):
    if not root:
        return [[]]
    if not root.left and not root.right:
        return [[root.val]]
    queue = [root]
    ans = [[root.val]]
    while queue:
        temp = []
        anst = []
        for i in queue:
            print(i.left)
            if i.left:
                anst.append(i.left.val)
                temp.append(i.left)
            if i.right:
                anst.append(i.right.val)
                temp.append(i.right)
        queue = temp
        if anst:
            ans.append(anst)
    return ans


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.left.left = TreeNode(4)
# root.left.right.right = TreeNode(5)

print(bfs(root))
