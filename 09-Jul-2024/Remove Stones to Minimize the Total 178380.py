# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Create a max-heap using negative values
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Pop the largest element (smallest negative value)
            largest = -heapq.heappop(max_heap)
            
            # Remove floor(largest / 2) stones
            reduced = largest - (largest // 2)
            
            # Push the reduced value back into the heap
            heapq.heappush(max_heap, -reduced)
        
        # Calculate the remaining total stones
        return -sum(max_heap)
