class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
            Does it makes sense to delete longest string possible 
            odd + even = odd
            so if alice does not pick longest , then bob gets to pick even 
            and bob must pick longest even so alice get's none
        """

        arr = []
        temp = 0
        for k in s:
            if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
                temp += 1
            arr.append(temp)
        if temp == 0:
            return False
        return True
        
        right = len(arr) - 1
        alice_turn = True
        while(right >= 0):
            is_odd = True
            if arr[right] % 2 == 0:
                is_odd = False
            if alice_turn:
                return

            

        
