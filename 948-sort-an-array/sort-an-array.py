class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case for recursion
        if len(nums) <= 1:
            return nums
        
        # Divide the array into two halves
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        # Merge the two sorted lists into a single sorted list
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # If there are remaining elements in left or right, append them
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
