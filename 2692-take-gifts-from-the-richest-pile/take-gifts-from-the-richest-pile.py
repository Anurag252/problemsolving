class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = []
        for m in gifts:
            heapq.heappush(q, -m)
        
        while(k > 0):
            gift = -heapq.heappop(q)
            heapq.heappush(q, -floor(sqrt(gift)))
            k -= 1
        return -sum(q)

        