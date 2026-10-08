class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set = len(set(nums))

        return len_nums != len_set