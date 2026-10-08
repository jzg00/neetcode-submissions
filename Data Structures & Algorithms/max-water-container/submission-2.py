class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (r-l) * min(heights[l], heights[r]), where l and r are two different bar indices
        # and we want to find the max area
        # if we use two pointers we can continue searching for the max area by moving the shorter bar;
        # this gives a chance to find a higher max area

        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area