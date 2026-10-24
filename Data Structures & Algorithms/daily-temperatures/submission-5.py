class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # pre-size result array with default values of 0
        stack = []  # holds the previous days waiting to be resolved

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: # when a temperature is warmer than the top of our stack
                idx = stack.pop()       # pop and store the index of the cooler previous temp
                result[idx] = i - idx   # calculate how many days passed and store in the correct location in result array
            
            stack.append(i) # push the index so we can calculate 'result[idx]'

        return result