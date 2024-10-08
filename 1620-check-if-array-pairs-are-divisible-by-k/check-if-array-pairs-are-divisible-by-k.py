class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}
        for m in arr:
                if m%k == 0:
                    continue
                if m%k in dic:
                    dic[m%k] += 1
                else:
                    dic[m%k] = 1
        for m,v in dic.items():
            if m == k/2 and k % 2 == 0 and v % 2 != 0:
                return False
            if k-m not in dic or v != dic[k-m]:
                return False

        return True


            

        