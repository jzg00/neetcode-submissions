class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using O(log n) binary search
        # if nums[mid] is greater than nums[r], then the min element has to be in the right half
        # else, the min element is in the left half
        # once l == r, return nums[l] as this is the min element
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid # not (mid - 1) since it's possible that nums[mid] is the min element
        
        return nums[l]