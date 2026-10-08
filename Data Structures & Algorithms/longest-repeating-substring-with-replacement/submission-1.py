class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0
        mostFreq = 0
        
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            mostFreq = max(mostFreq, count[s[r]])

            if (r - l + 1) - mostFreq > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest