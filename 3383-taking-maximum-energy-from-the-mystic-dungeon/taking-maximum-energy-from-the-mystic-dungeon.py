class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
            if you start with i and move to i + k, 
            T[i] = max(T[i-k] , a[i])
            T[i] = a[i] where i <= k 
        """
        T = energy.copy()
        for i, m in enumerate(energy):
            if i - k < 0:
                T[i] = m
                continue 
            T[i] = max(T[i], m + T[i-k])
        return max(T[-k:])

        