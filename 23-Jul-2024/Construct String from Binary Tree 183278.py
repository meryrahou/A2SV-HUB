# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def preorder(node):
            if not node:
                return ""
            
            result = str(node.val)
            
            if node.left or node.right:
                result += "(" + preorder(node.left) + ")"
            
            if node.right:
                result += "(" + preorder(node.right) + ")"
                
            return result
        
        return preorder(root)