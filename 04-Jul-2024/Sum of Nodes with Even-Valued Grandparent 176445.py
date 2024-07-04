# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(vertex, parent=None, grandparent=None):
            if vertex == None :
                return 0
            
            s = 0
            if grandparent and grandparent.val % 2 == 0 :
                s += vertex.val 
            
            s += dfs(vertex.left, vertex, parent)
            s += dfs(vertex.right, vertex, parent)
            return s
        
        return dfs(root)