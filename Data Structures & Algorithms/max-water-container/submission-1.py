class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (r-l) * min(height[l], height[r]), where l and r are two different bar indices
        # and we want to find the max area

        max_area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                max_area = max(max_area, area)
            
        return max_area
    