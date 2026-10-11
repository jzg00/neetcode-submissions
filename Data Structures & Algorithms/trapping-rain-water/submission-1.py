class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0
        
        l, r = 0, len(height) - 1
        leftWall = rightWall = 0
        total = 0

        while l < r:
            leftWall = max(leftWall, height[l])
            rightWall = max(rightWall, height[r])

            if height[l] <= height[r]:
                total += leftWall - height[l]
                l += 1
            else:
                total += rightWall - height[r]
                r -= 1
            
        return total