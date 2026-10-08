class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        output = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        seen.add((nums[i], nums[j], nums[k]))
        
        return list(seen)