class Solution:
    def maxArea(self, height: list[int]) -> int:

        max_area, i, j = 0, 0, len(height) - 1

        while i < j:
            altitude = min(height[i], height[j])
            width = j - i
            area = altitude * width
            max_area = max(area, max_area)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1


        return max_area
        
        