class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # invariant: the window never contains a repeat. When a new character would create one, 
        # shrink from the left just enough to drop the old copy, then add the new one.
        left = longest = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest