class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for c in s:
            if c.isalnum():
                new += c
        
        new = new.lower()

        return new == new[::-1]