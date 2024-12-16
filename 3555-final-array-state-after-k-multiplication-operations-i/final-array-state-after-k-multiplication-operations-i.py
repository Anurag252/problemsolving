class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []

        for idx, m in enumerate(nums):
            heapq.heappush(h, (m, idx))
        
        while(k > 0):
            (item, idx) = heapq.heappop(h)
            heapq.heappush(h, (item * multiplier , idx))
            k -= 1
        h.sort(key= lambda x : x[1])
        return list(map(lambda x : x[0], h))
        

        