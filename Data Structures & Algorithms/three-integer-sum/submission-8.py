class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            fixed = nums[i]
            left, right = i+1, len(nums) - 1
            while left < right:
                if fixed + nums[left] + nums[right] == 0:
                    res.add((fixed, nums[left], nums[right]))
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                elif fixed + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(res)
                
        # res = ((-1, -1, 2),(-1, 0, 1))
        # nums = [-4, -1, -1, 0, 1, 2]
        # i = 1
        # fixed = -1
        # left = 2 , right = 5
        # sum = -1 + (-1) + 2 = 0