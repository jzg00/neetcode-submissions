class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # to avoid redundant checks
            if num - 1 in nums_set:
                continue
        
            current = num
            streak = 1
            while current + 1 in nums_set:
                streak +=1
                current += 1
            
            longest = max(longest, streak)

        return longest