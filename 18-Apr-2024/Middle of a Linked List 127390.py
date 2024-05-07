# Problem: Middle of a Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        jumper1 = head
        jumper2 = head
        while jumper2 and jumper2.next:
            jumper1 = jumper1.next
            jumper2 = jumper2.next.next
        
        return jumper1
        