class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        result = []
        for k in timePoints:
            hour = k.split(":")[0]
            minute = k.split(":")[1]
            total = int(hour) * 60 + int(minute)
            result.append(total)
        
        result.sort()
        diff = 1440
        start = 1
        end = len(result)
        while(start < end):
            diff = min(diff, result[start] - result[start-1])
            start += 1
        
        diff = min(diff, result[0] + 1440 - result[-1])
        return diff

        