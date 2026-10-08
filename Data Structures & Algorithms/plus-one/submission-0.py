class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)
        
        new = str(int(s) + 1)
        res = []
        for n in new:
            res.append(int(n))
        
        return res