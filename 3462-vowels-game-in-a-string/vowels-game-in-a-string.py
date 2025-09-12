class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
            Does it makes sense to delete longest string possible 
            odd + even = odd
            so if alice does not pick longest , then bob gets to pick even 
            and bob must pick longest even so alice get's none
        """


        for k in s:
            if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
                return True
        return False
        

            

        
