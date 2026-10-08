class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early check: if the len(s) != len(t) they can't be anagrams of eachother
        if len(s) != len(t):
            return False
        
        # store the frequency of each char for each input string
        count_s, count_t = collections.defaultdict(int), collections.defaultdict(int)

        # since we know s and t are the same length, we can use either for the range
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        
        return count_s == count_t


    # Input: s = "racecar", t = "carrace"

    # count_s = {'r': 2, 'a': 2, 'c': 2, 'e': 1,}
    # count_t = {'c': 2, 'a': 2, 'r': 2,'e': 1,}


    