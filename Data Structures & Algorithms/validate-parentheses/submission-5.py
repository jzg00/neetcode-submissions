class Solution:
    def isValid(self, s: str) -> bool:
        # stack: LIFO
        # solution:
        # use a hashmap to store the closed parentheses as keys, and their respective open parentheses as values
        # initialize a stack using an empty array
        # for each char in s:
        # if char is a closing parentheses, if the stack is empty or they don't match, return False.
        # check if the last element in stack is its corresponding open parentheses:
        # if yes, pop from the stack. 
        # if char is an opening parentheses, push to stack 
        # if we've iterated through all of s, and our stack is empty: return True

        pairs = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
