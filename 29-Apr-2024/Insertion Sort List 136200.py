# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))  
        curr = head
        
        while curr:
            prev, next_node = dummy, dummy.next
            while next_node and next_node.val < curr.val:
                prev, next_node = next_node, next_node.next
            
            prev.next, curr.next, curr = curr, next_node, curr.next
        
        return dummy.next
