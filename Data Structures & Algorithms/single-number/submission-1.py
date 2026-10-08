class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # optimal solution O(n) time O(1) extra space using XOR

        res = 0

        for num in nums:
            res ^= num
        
        return res