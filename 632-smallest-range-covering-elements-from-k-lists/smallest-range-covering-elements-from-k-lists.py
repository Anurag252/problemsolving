class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for idx, k in enumerate(nums):
            for l in k:
                arr.append((l, idx))

        arr.sort(key=lambda x : x[0])
        #print(arr)

        dic = {}

        for idx, k in enumerate(nums):
            dic[idx] = 0
        left = -1
        right = 0
        result = [1,10** 5]
        #print(dic)

        def is_valid():
            for k,v in dic.items():
                if v == 0:
                    return False
            return True

        def compare(result, left, right):
            if result[1] - result[0] <= arr[right][0] - arr[left][0]:
                return result
            else:
                #print([arr[left][0], arr[right][0]] , "here")
                return [arr[left][0], arr[right][0]]

        def is_all_plus(left):
            if left -1 < 0:
                return True

            return dic[arr[left -1][1]] > 1


        while(left <= right and right < len(arr)):
            #print(dic, left, right)
            dic[arr[right][1]] += 1

            if is_valid():
                result = compare(result, left, right)

            while (is_all_plus(left + 1)):
                if left >= 0:
                    dic[arr[left][1]] -= 1
                left += 1
            if is_valid():
                result = compare(result, left, right)
                #print(result, "result")
            right += 1

        return result
            


        
        #[a,b,c]

        #incr always
        #dec if after dec we are at least 1,1,1