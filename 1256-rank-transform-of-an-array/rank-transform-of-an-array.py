class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_cpy = arr.copy()
        arr.sort()
        #print(arr, arr_cpy)
        result = [0] * len(arr)
        dic = {}
        temp = 0

        for idx, k in enumerate(arr) :
            if idx > 0 and k == arr[idx-1]:
                continue
            else:
                temp +=1
                dic[k] = temp

        for idx, k in enumerate(arr_cpy) :
            result[idx] = dic[k]

        return result
            

            


        