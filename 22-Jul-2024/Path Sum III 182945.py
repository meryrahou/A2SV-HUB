# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0  
        
        def dfs(node: TreeNode, current_sum: int):
            if not node:
                return
            
            checkPathSum(node, current_sum)
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        def checkPathSum(node: TreeNode, current_sum: int):
            if not node:
                return
            
            current_sum += node.val

            if current_sum == targetSum:
                self.count += 1
            
            checkPathSum(node.left, current_sum)
            checkPathSum(node.right, current_sum)
        
        dfs(root, 0)
        
        return self.count