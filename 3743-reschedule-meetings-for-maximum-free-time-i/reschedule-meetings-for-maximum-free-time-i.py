from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []

        # Gap before first meeting
        gaps.append(startTime[0] - 0)

        # Gaps between meetings
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])

        # Gap after last meeting
        gaps.append(eventTime - endTime[-1])

        # Sliding window over gaps
        max_total = 0
        total = 0
        left = 0

        for right in range(len(gaps)):
            total += gaps[right]

            # If merges needed > k, shrink window
            while right - left > k:
                total -= gaps[left]
                left += 1

            max_total = max(max_total, total)

        return max_total
