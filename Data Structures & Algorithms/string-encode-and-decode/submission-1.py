class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded 
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1   # i moves to the start of the beginning of the string
            j = i + length
            decoded.append(s[i:j])

            i = j   # move i to the length of the next string
        
        
        return decoded



# strs = ["hello", "world"]
# encoded = "5#hello5#world"
# decoded = ["hello", "world"]

