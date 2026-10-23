class MinStack:

    def __init__(self):
        self.stack = [] # each object instance gets its own stack

    def push(self, val: int) -> None:
        if not self.stack:
            minVal = val    # if the stack is empty, the newmin is just the value being pushed
        else:
            minVal = min(self.stack[-1][1], val)   # if the stack isn't empty, new min becomes min of the current min or new value
        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
