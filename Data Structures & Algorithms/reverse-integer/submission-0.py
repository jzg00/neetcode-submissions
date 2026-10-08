class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        copy = abs(x)
        res = 0

        while copy != 0:
            digit = copy % 10
            res = res * 10 + digit
            copy //= 10
        
        if res < INT_MIN or res > INT_MAX:
            return 0
        
        return -res if x < 0 else res