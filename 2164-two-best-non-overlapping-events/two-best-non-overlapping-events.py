class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key= lambda x : (x[0],x[1]) )

        arr = [0]
        temp = 0
        events.reverse()
        for k in events:
            temp = max(temp, k[2])
            arr.append(temp)
        events.reverse()
        arr.reverse()
        
        
        def good(idx, mid):
            if events[idx][1] < events[mid][0]:
                return True
            return False


        ans = 0
        events.append([10**6, 10**6,0])


        for idx, k in enumerate(events):
            left = idx + 1
            right = len(events) - 1
            while(left < right):
                mid = (right + left) // 2
                if good(idx, mid):
                    print("yes")
                    right = mid
                else:
                    left = mid + 1
            if right == len(events) - 1 :
                ans = max(ans , k[2] ) # this is overlapping all further intervals
            else:
                ans = max(ans , k[2] + arr[left]) # got two maximums 
            print(idx, ans, left)
        return ans