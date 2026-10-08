class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    # encoded = '4#neet4#code4#love3#you'

    def decode(self, encoded: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(encoded):
            j = i
            while encoded[j] != '#':
                j += 1
            
            length = int(encoded[i:j])
            i = j + 1
            j = i + length

            decoded.append(encoded[i:j])

            i = j
        
        return decoded