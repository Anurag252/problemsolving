class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort(key=lambda x : (x[0], x[1]))
        print(meetings)

        count = -1
        start = 0
        end = 0
        for k in meetings:
            print(start, end, count)
            if end < k[0]:
                count += (end - start + 1)
                start = k[0]
                end = k[1]
            else:
                end = max(k[1], end)
        print(start, end, count)
        count += (end - start + 1)
        return days - count
        