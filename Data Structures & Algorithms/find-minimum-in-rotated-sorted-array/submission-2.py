class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force O(n)

        min_val = float('inf')
        for num in nums:
            if num < min_val:
                min_val = num
        
        return min_val
