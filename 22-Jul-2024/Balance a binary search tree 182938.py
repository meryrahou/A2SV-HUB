# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node: TreeNode) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        sorted_nodes = inorder_traversal(root)
        
        def build_balanced_bst(nodes: List[TreeNode], start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = (start + end) // 2
            root = nodes[mid]
            root.left = build_balanced_bst(nodes, start, mid - 1)
            root.right = build_balanced_bst(nodes, mid + 1, end)
            return root
        
        return build_balanced_bst(sorted_nodes, 0, len(sorted_nodes) - 1)