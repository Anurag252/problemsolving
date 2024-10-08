class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        k = 1
        curr_count = 1
        currr_elem = s[0]
        result = ""
        while(k < len(s)):
            if s[k] == s[k-1]:
                curr_count += 1
            else:
                result += (str(curr_count) + str(currr_elem))
                curr_count = 1
                currr_elem = s[k]
            k += 1
        result += str(curr_count) + str(currr_elem)
        return result


