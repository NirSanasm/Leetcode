class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, value: int) -> None:

        if self.getMin() is None:
            self.items.append([value, value])
        else:
            val = self.getMin()
            if val <= value:
                self.items.append([value, val])
            else:
                self.items.append([value, value])

        

    def pop(self) -> None:
        self.items.pop()
        

    def top(self) -> int:
        return self.items[-1][0]
        

    def getMin(self) -> int:
        return self.items[-1][-1] if self.items else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()