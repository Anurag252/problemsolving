class MyCalendarTwo:

    def __init__(self):
        self.cal = []

        

    def book(self, start: int, end: int) -> bool:
        overlap = []

        for  idx1, k in enumerate(self.cal):
            if k[0] <= start and start < k[1]:
                s = start
                e = min(end, k[1])
                for idx2,l in enumerate(self.cal):
                    if l[0] <= s and s < l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and e <= l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and l[0] >= s and idx1 != idx2:
                        return False

            elif k[0] < end and end <= k[1]:
                s = max(k[0],start)
                e = end
                for idx2,l in enumerate(self.cal):
                    if l[0] <= s and s < l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and e <= l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and l[0] >= s and idx1 != idx2:
                        return False

            elif k[0] < end and k[0] >= start:
                s = k[0]
                e = k[1]
                for idx2,l in enumerate(self.cal):
                    if l[0] <= s and s < l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and e <= l[1] and idx1 != idx2:
                        #print(start, end, l[0], l[1], s , e)
                        return False
                    if l[0] < e and l[0] >= s and idx1 != idx2:
                        return False

        self.cal.append((start, end))
        return True
        

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)