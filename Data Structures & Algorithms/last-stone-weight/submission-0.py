class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # since we have a max heap, s1 will always be >= s2
            s1, s2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if s1 > s2:
                heapq.heappush(maxHeap, (-s1) - -(s2))
            
        return -maxHeap[0] if maxHeap else 0