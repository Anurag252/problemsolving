class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        result =[]
        for k in s1.split():
            if k not in dic:
                dic[k] = 1
            else :
                dic[k] += 1

        for k in s2.split():
            if k not in dic:
                dic[k] = 1
            else :
                dic[k] += 1

        for k,v in dic.items():
            if v == 1:
                result.append(k)
        
        return result

