
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Map to maintain sorted frequency map of current window
        freq = {}
        left = right = 0
        count = 0  # Total count of valid subarrays

        while right < len(nums):
            # Add current element to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1
            right += 1

        return count


"""
        left = 0
        right = 0
        arr = []
        result = 0



        def valid_range(n, arr):
            if len(arr) == 0:
                arr.append(n)
                return True
            if len(arr) == 1:
                if arr[0] + 2 <= n or arr[0] - 2 <= n:
                    arr.append(n)
                    arr.sort()
                    return True
                else:
                    return False
            if len(arr) == 2:
                return n in arr

        def not_valid(left , right ,  arr):

            while(right > left):

            


        def add(t):
            count = 0
            for k in range(t+1):
                count += k
            return count

        while(left < len(nums) and right < len(nums)):
            print(left, right, arr)
            if valid_range(nums[right], arr):
                right += 1
            else:
                result += add(right - left)
                arr = []
                while(not_valid(left, right, arr)):
                    left += 1
        return result

        """