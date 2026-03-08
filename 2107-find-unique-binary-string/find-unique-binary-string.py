class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr = []
        s = set()
        v = 0
        for k in nums:
            arr.append(int(k, 2))
            s.add(int(k, 2))
        #print(arr)
        for k in range(0, pow(2,len(nums[0]))):
            if k not in s:
                v = k
                break
        x = format(v, 'b')
        #print(x)
        if len(nums[0]) > len(str(x)):
            return ("0" * (len(nums[0]) - len(str(x)))) + str(x)
        return str(x)
        


