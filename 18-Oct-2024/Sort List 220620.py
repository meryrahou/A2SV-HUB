# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        # split list into two, using fast and slow pointer
        middle = self.getmid(head)

        half1 = head

        half2 = middle.next
        middle.next = None

        # sort the two halves
        half1 = self.sortList(half1)
        half2 = self.sortList(half2)

        return self.merge(half1, half2)

    def getmid(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, half1 : ListNode, half2 : ListNode) -> ListNode:
        dummy = ListNode()

        tail = dummy

        while half1 and half2 :
            if half1.val < half2.val:
                tail.next = half1
                half1 = half1.next
            else :
                tail.next = half2
                half2 = half2.next
            
            tail = tail.next

        if half1:
            tail.next = half1
        elif half2 :
            tail.next = half2
        
        return dummy.next
