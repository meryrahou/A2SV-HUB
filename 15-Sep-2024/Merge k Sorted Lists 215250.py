# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                                  # (node value, index of list, node itself)
                heapq.heappush(heap, (lists[i].val, i, lists[i]) )
        
        dummy_head = ListNode(0)
        current = dummy_head

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = ListNode(val)
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy_head.next