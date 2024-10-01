class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}
        for m in arr:
            if k - (m%k) in dic:
                dic[k - (m%k)] -= 1
            else:
                if m%k in dic:
                    dic[m%k] += 1
                else:
                    dic[m%k] = 1
        print(dic)
        for m,v in dic.items():
            if v != 0 and m != 0:
                if k % 2 == 0 and m == k / 2 and v % 2 == 0:
                    continue
                else:
                    return False
        return True

            

        