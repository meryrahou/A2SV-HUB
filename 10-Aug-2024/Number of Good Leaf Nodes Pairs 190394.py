# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            # If the node is a leaf
            if not node.left and not node.right:
                return [1]
            
            # Get distances from the left and right children
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good pairs between the two subtrees
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        nonlocal good_pairs
                        good_pairs += 1
            
            # Return updated distances, incrementing each by 1
            return [d + 1 for d in left_distances + right_distances if d + 1 < distance]

        good_pairs = 0
        dfs(root)
        return good_pairs
