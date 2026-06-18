"""Trapping Rain Water"""

class Solution:
    def trap(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1

        left_max = 0
        right_max = 0
        total_water = 0

        while start < end:
            left_max = max(left_max, height[start])
            right_max = max(right_max, height[end])

            if left_max < right_max:
                # The point at which start is pointing we know how much water will store here
                total_water += left_max-height[start]
                start +=1
            
            else:
                # Either they are equal or right max is smaller
                # NOTE: right max will always be >= end
                # NOTE: left max will always be >= start -> Hence right_max - height[end] and  left_max-height[start] will either give zero or positive values
                total_water += right_max - height[end]
                end -=1
        
        return total_water
        