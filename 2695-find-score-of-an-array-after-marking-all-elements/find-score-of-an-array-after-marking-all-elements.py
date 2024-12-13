class Solution:
    def findScore(self, nums: List[int]) -> int:
        s = set()

        h = []

        for idx, k in enumerate(nums):
            heapq.heappush(h, (k, idx))
        score = 0
        while(len(h) > 0):
            item = heapq.heappop(h)
            if item[1] not in s:
                s.add(item[1])
                s.add(item[1] + 1)
                s.add(item[1] - 1)
                score += item[0]
        return score

        