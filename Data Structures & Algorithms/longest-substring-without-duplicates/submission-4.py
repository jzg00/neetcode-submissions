class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # small optimization using a hashmap
        seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1 , left)
            seen[s[right]] = right
            longest = max(longest, right - left + 1)
        
        return longest