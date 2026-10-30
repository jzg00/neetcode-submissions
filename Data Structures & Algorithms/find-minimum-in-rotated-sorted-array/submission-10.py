class Solution:
    def findMin(self, nums: List[int]) -> int:
        current_min = float('inf')
        for num in nums:
            if num < current_min:
                current_min = num
        
        return current_min