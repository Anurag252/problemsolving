class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = {}
        for k in nums:
            if k in h:
                h[k] = h[k] + 1
            else:
                h[k] = 1
        m =[]
        for k in h:
            m.append((k, h[k]))
        sign = ""
            
        m.sort(key=lambda x: (x[1], -x[0])) 
        
        result =[]
        for k in m:
            for l in range(k[1]):
                result.append(k[0])
        return result

            
        
        