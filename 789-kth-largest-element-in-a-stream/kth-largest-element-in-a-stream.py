class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.limit = k
        for l in nums:
            heapq.heappush(self.h, l)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.limit:
            heapq.heappop(self.h)
        return self.h[0]
        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)