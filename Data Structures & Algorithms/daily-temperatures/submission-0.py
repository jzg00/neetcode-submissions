class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = []

        for i in range(n):
            j = i + 1
            while j < n:
                if temperatures[j]  > temperatures[i]:
                    break
                j += 1            
            if j == n:
                output.append(0)
            else:
                output.append(j - i)
        
        return output