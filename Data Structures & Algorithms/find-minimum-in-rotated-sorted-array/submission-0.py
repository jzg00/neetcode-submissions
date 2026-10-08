class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force O(n)

        min_val = float('inf')

        for num in nums:
            min_val = min(min_val, num)
        
        return min_val
