class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want to maxiumize the amount of water or the area
        # width = r - l , height = min(height[l], height[r])
        # area = width * height

        l, r = 0, len(heights) - 1
        currentMax = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            currentMax = max(currentMax, area)

            if heights[l] < heights[r] or heights[l] == heights[r]:
                l += 1
            else:
                r -= 1
            
        return currentMax