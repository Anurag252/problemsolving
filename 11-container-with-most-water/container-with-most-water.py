class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current width
            width = right - left
            
            # Determine current height (limited by the shorter line)
            current_height = min(height[left], height[right])
            
            # Calculate current area
            current_area = width * current_height
            
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area