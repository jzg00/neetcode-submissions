class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using O(log n) binary search
        # if mid val is greater than both l and r vals, search side with lesser val
        # if mid val is less than than both l and r vals, search side with greater val
        # if mid == l or mid == r, return the min of the two
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]