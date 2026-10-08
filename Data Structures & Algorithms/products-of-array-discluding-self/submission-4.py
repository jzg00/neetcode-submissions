class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                totalProduct *= num
            else:
                zeroCount += 1
        
        if zeroCount > 1:
            return [0] * len(nums)


        output = [0] * len(nums)
        for i in range(len(nums)):
            if zeroCount == 1:
                if nums[i] == 0:
                    output[i] = totalProduct
            else:
                output[i] = totalProduct // nums[i]
        
        return output