class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            current_min = self.stack[-1][1]
            new_min = min(current_min, val)
            self.stack.append([val, new_min])
        

    def pop(self) -> None:      
        self.stack.pop()


    def top(self) -> int:
        if len(self.stack) == 0:
            return None  
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()