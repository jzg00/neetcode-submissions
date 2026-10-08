class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # store the end index for each char in s
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        
        output = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, lastIdx[c])

            if i == end:
                output.append(end - start + 1)
                start = end + 1
        
        return output