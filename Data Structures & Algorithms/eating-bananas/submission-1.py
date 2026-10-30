class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # at most, k would be the max(piles)
        # calculate total hours it will take to eat all piles at rate k
        # if those total hours <= h, lower k and recalculate total hours
        # if total hours > h, then we don't use that k

        # total_hours = ceil(piles[i] / k)

        # this is inefficient if we keep lowering k by 1 and check everytime
        # we can use binary search to find a k that is within those bounds

    
        # set our bounds to run binary search for k
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
            
            if total_hours <= h:
                r = k
            else:
                l = k + 1
        
        return (l)
