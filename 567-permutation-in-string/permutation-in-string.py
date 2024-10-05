class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start = 0
        end = len(s1)-1
        arr_old = [0] * 26
        arr_new = [0] * 26
        for k in s1:
            arr_old[ord(k)-97] += 1
        for k in s2[start:end+1]:
            arr_new[ord(k)-97] += 1
        #print(arr_new)
        while(end < len(s2)-1):
            if ''.join(map(str,arr_old)) == ''.join(map(str,arr_new)):
                return True
            #print(''.join(map(str,arr_old)), ''.join(map(str,arr_new)))
            arr_new[ord(s2[start]) - 97] -= 1
            start += 1
            end += 1
            arr_new[ord(s2[end]) - 97] += 1
        if ''.join(map(str,arr_old)) == ''.join(map(str,arr_new)):
                return True 
        return False
        
        