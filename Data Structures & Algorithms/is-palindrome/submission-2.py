class Solution:
    def isPalindrome(self, s: str) -> bool:
        # recreate s in a new string
        new_s = ''
        # iterate through each char in s and add it to the new str if its alphanumeric
        for c in s:
            if c.isalnum():
                new_s += c
        # convert the new string to lowercase
        new_s = new_s.lower()
        # compare new string to itself in reverse (returns true if its a palindrome)
        return new_s == new_s[::-1]