# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = storage1 = list1
        ptr2 = storage2 = list2

        if not ptr1:
            return ptr2
        if not ptr2:
            return ptr1

        if ptr1.val <= ptr2.val:
            head = ptr1
            ptr1 = ptr1.next
        else:
            head = ptr2
            ptr2 = ptr2.next

        current = head

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next

        if ptr1:
            current.next = ptr1
        elif ptr2:
            current.next = ptr2

        return head
