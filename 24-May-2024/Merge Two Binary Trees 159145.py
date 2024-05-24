# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r1 and not r2:
            return None
        elif not r1:
            return r2
        elif not r2:
            return r1

        root = TreeNode(r1.val + r2.val)
        root.left = self.mergeTrees(r1.left, r2.left)
        root.right = self.mergeTrees(r1.right, r2.right)
        
        return root
