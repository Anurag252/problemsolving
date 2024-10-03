class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = []
        suffix_sum = []
        temp = 0
        for k in nums:
            temp += k
            prefix_sum.append(temp%p)
            
        #prefix_sum.append(temp)

        temp = 0
        for k in nums[::-1]:
            temp += k
            suffix_sum.append(temp%p)
            
        #suffix_sum.append(temp)

        map = {}
        result = 10**5
        print(prefix_sum, suffix_sum)
        for idx,k in enumerate(prefix_sum):
            if k == 0:
                result = min(result, len(nums) - idx-1)
            if k in map:
                map[k].append(idx)
            else:
                map[k] = [idx]
        print(prefix_sum, suffix_sum[::-1], map, result)
        
        for idx,k in enumerate(suffix_sum[::-1]):
            if k == 0:
                result = min(result, idx)
            if p-k in map:
                for m in map[p-k]:
                    if m < idx:
                        result = min(result, idx-m-1)
        return result if result < 10 ** 5 else -1





        