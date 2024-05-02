class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)
        for item in points:
            dist = item[0]*item[0] + item[1]*item[1]
            heapq.heappush(arr, (dist, item))
        result = []
        for i in range(k):
            (dist, item) = heapq.heappop(arr)
            print(item)
            result.append(item)
        
        return result
        