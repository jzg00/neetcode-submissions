class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # check if the left half is sorted
            if nums[l] <= nums[m]:
                # check if target is in the left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # else, the right half is sorted
            else:
                # check if target is in the right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1