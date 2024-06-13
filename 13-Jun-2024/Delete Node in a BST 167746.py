# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val

            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def getMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
