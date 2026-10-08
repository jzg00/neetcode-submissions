class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # empty set
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False