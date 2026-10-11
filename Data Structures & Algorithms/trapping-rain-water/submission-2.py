class Solution:
    def trap(self, height: List[int]) -> int:
        # Precompute the max wall height on each side using two arrays
        # formula to calculate the water trapped at any position i:
        # min(leftMax, rightMax) - height[i]

        n = len(height)
        if len(height) < 3:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, len(leftMax)):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        rightMax[-1] = height[-1]
        for i in range(len(rightMax) - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])
        
        total = 0
        for i in range(n):
            total += min(leftMax[i], rightMax[i]) - height[i]
        
        return total