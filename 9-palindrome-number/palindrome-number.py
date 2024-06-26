class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x != ceil(x):
            return False
        if x == 0:
            return True
        inverted_num = 0
        orig = x
        m = 1
        n = pow(10,int(log(x,10)))
        while(x >= 0 and n >= 1):
            
            l = int(x / n)
            print(l,inverted_num, n,m,x)
            inverted_num = inverted_num + l*m
            x = int(x % n)
            n = int(n / 10)
            m = m * 10
        return inverted_num == orig



        