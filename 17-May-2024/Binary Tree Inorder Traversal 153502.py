# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def PreOrder(p):
            if not p:
                return
            PreOrder(p.left)
            vals.append(p.val)
            PreOrder(p.right)

        PreOrder(root)

        return vals