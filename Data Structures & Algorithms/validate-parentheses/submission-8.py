class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]" : "[", ")" : "(", "}" : "{"}

        for c in s:
            if c in pairs: # if c is a closed parentheses
                if not stack or stack[-1] != pairs[c]: # if the stack is empty or if c doesn't match the last opening parentheses
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack