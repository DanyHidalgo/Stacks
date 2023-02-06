
class Stack:

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top = -1


    def __repr__(self) -> str:
        return "Top: {} | Elements: {}".format(self.top, self.elements)
    

    def push(self, value: str) -> None:
        if self.top == len(self.elements) - 1:
            raise Exception("Stack Overflow :(")

        self.top += 1
        self.elements[self.top] = value

    
    def pop(self) -> str:
        if self.top == -1:
            raise Exception("Stack Underflow :(")

        value = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1
        return value

    
    def peek(self) -> str:
        if self.top == -1:
            raise Exception("Stack Underflow :(")
        
        value = self.elements[self.top]
        return value

