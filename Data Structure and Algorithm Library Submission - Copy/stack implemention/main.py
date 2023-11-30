class Stack:
    def __init__(self, n):
        self.data = [None] * n
        self.top = 0
        self.max_size =n

    def push(self, val):
        if self.length() < self.max_size:
            self.data[self.top] = val
            self.top += 1

    def pop(self):
        if self.is_empty() == False:
            temp = self.data[self.top - 1]
            self.data[self.top - 1] = None
            return temp

    def top(self):
        return self.data[self.top - 1]

    def length(self):
        return self.top

    def is_empty(self):
        return self.top == 0

    def printStack(self):
        print(self.data)

print('Tests for Stack Implementation')
test_stack = Stack(9)



S = Stack(10)
S.is_empty()
S.pop()
S.push(5)
S.push(50)
S.push(500)
S.printStack()
S.pop()
S.pop()
S.length()
S.push(100)
S.printStack()
S.is_empty()