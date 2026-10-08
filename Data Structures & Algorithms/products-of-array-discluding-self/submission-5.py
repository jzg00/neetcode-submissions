class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Pass 1: res[i] = product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply in the product of everything to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res