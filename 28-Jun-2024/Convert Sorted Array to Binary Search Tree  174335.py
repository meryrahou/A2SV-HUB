# Problem: Convert Sorted Array to Binary Search Tree  - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def convertListToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)
            return node
        
        return convertListToBST(0, len(nums) - 1)
