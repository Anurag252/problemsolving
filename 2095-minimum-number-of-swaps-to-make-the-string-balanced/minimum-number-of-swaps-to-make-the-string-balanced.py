class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        balance = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else:  # char == ']'
                balance -= 1
            
            # If balance goes negative, we have more ] than [ so far
            if balance < 0:
                imbalance += 1
                balance = 0  # Reset balance to zero to continue counting fresh

        # Each swap fixes two misplacements
        return (imbalance + 1) // 2
        
  
#T[o,n] = T[1,n-1] + 1 if s[0], s[n] makes a bracket , else T[1,n-1] or inf
#T[0,n] = T[0,n-2] + 1   if s[n-1] + s[n] does not make a bracket else T[0, n-2] of inf

      