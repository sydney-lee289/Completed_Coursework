# in class deque implementation
class Deque:
    def __init__(self, n):
        self.data = [None] * n
        self.max_size = n
        self.length = 0
        self.first = n-1
        self.last = 0

    def add_first(self, val):
        self.data[self.first] = val
        self.first = (self.first - 1) % self.max_size
        self.length += 1

    def add_last(self, val):
        self.data[self.last] = val
        self.last = (self.last + 1) % self.max_size
        self.length += 1

    def delete_first(self):
        self.first = (self.first + 1) % self.max_size
        temp = self.data[self.first]
        self.data[self.first] = None
        self.length -= 1
        return temp

    def delete_last(self):
        if self.length == 0:
            print('error')
            return
        self.last = (self.last - 1) % self.max_size
        temp = self.data[self.last]
        self.data[self.last] = None
        self.length -= 1
        return temp

    def lennie (self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def print_deque(self):
        i = (self.first + 1)% self.max_size
        while (self.data[i] != None):
            print(self.data[i], end = " ")
            i = (i + 1)% self.max_size
        print("")

print('Test for Deque Implementation')

D = Deque(10)

D.delete_last()
D.add_last(50)
D.add_first(2)
D.print_deque()
D.delete_last()
D.print_deque()
D.add_first(10)
D.add_first(100)
D.add_last(1)
D.print_deque()
D.delete_last()
D.delete_first()
D.lennie()
D.print_deque()






