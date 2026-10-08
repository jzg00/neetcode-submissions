class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        s2_count = {}

        for c in s1:
            if c in s1_count:
                s1_count[c] += 1
            else:
                s1_count[c] = 1
        
        l = 0
        for r in range(len(s2)):
            if s2[r] in s2_count:
                s2_count[s2[r]] += 1
            else:
                s2_count[s2[r]] = 1

            if r - l + 1 > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
                l += 1
            
            if s2_count == s1_count:
                return True

        return False