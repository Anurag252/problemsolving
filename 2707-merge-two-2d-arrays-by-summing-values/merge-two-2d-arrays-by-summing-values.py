class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = {}

        mx = 0

        for k in nums1:
            mp[k[0]] = k[1]
            mx = max(mx, k[0])

        for k in nums2:
            if k[0] not in mp:
                mp[k[0]] = k[1]
            else:
                mp[k[0]] += k[1]
            mx = max(mx, k[0])
        
        res = []

        for k in range(1,mx+1):
            if k in mp:
                res.append([k, mp[k]])
        return res

