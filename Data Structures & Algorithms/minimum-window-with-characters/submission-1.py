class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # optimal solution using sliding window O(n + m)

        if len(t) > len(s): 
            return ""
        
        need = collections.defaultdict(int)
        for char in t:
            need[char] += 1
        
        required = len(need)
        have = collections.defaultdict(int)
        satisfied = 0
        best_len = float('inf')
        best_start = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            if c in need:
                have[c] += 1
                if have[c] == need[c]:
                    satisfied += 1

            while satisfied == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                
                d = s[left]
                if d in need:
                    have[d] -= 1
                    if have[d] < need[d]:
                        satisfied -= 1
                
                left +=1 
        
        if best_len == float('inf'):
            return ""
        else:
            return s[best_start:best_start + best_len]




            