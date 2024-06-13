# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.count = 0
        
        def in_order_traversal(node):
            if not node:
                return

            in_order_traversal(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            in_order_traversal(node.right)
        
        in_order_traversal(root)        
        return self.result
