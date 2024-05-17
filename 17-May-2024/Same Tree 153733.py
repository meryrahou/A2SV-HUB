# Problem: Same Tree - https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_true = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return self.is_true 

        val_q = q.val if q else None
        val_p = p.val if p else None

        if val_q != val_p:
            self.is_true = False
            return
        
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

        return self.is_true
