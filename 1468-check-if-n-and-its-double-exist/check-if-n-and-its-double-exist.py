class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = set()

        for k in arr:
            
            if k in dic:
                return True
            
            #print(dic)
            if k % 2 == 0: 
                dic.add(int(k//2))
            dic.add(k*2)
        
        return False



            

        