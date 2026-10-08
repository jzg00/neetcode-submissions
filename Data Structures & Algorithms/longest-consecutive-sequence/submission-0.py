class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)    # create a hash set of the nums (removes duplicates and allows for faster lookup)
        longest = 0             # variable to store the length of the longest consecutive sequence

        # iterate through each number in the set
        for num in nums_set:
            # find the start of the sequence (this helps to avoid redundant checks)
            if num - 1 in nums_set:
                continue
            
            # if we find the start of a sequence, we check check if there is a consecutive element for it
            # and update the streak
            curr = num
            streak = 1
            while curr + 1 in nums_set:
                streak += 1
                curr += 1

            longest = max(longest, streak)  # update the longest to either the current longest or the streak
        
        return longest