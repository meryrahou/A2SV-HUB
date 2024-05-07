# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        storage = dummy = ListNode(next=head)

        for _ in range(left - 1):
            storage = storage.next

        ptr = storage.next
        nxt = ptr.next

        for _ in range(right - left):
            ptr.next = nxt.next
            nxt.next = storage.next
            storage.next = nxt
            nxt = ptr.next

        return dummy.next
