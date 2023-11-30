class Queue:
    def __init__(self, n):
        self.data = [None] * n
        self.first = 0
        self.avail = 0
        self.length = 0
        self.max_size = n

    def enqueue(self, val):
        if self.length < self.max_size:
            self.data[self.avail] = val
            self.avail = (self.avail + 1) % self.max_size
            self.length += 1

    def dequeue(self):
        if self.is_empty() == False:
            temp = self.data[self.first]
            self.data[self.first] = None
            self.first = (self.first + 1) % self.max_size
            self.length -= 1
            return temp

    def first(self):
        return self.data[self.first]

    def is_empty(self):
        return self.length == 0

    def lennie(self):
        return self.length

    def print(self):
        print(self.data)

print('Tests for Queue Implementation')
test_queue = Queue(19)


test_queue.enqueue(25)
test_queue.print()
test_queue.dequeue()
test_queue.print()
print(test_queue.first)
test_queue.print()
print(test_queue.lennie())
print(test_queue.is_empty())
test_queue.print()