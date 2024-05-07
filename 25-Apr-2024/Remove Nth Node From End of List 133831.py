# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        position_from_start = length - n
        
        current = dummy
        for _ in range(position_from_start):
            current = current.next
        
        current.next = current.next.next
        
        return dummy.next
