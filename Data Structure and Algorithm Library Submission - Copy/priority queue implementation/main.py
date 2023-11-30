# priority queue in class implementation
# implement using a list instead of an array
'''
class Priority_Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def parent(self,i):
        return (i - 1) // 2 #why division by 2

    def left_child(self, i):
        return (2 * i) +1

    def right_child(self, i):
        return (2 *i) + 2

    def add_item(self, key, value):
        self.data.append((key, value))
        self.upheapBubble(len(self.data) - 1)
        self.length += 1

    def upheapBubble(self, index):   #store key and value as a tuple
        if index > 0:
            parentIndex = self.parent(index)
            if self.data[parentIndex][0] > self.data[index][0]:
                self.data[index], self.data[parentIndex] = self.data[parentIndex], self.data[index ]#swaps
                self.upheapBubble(parentIndex)
            else:
                return

    def removeMin(self):    # O(1)
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        item = self.data.pop()
        self.downheapBubble(0)
        self.length -= 1 
        return item

    def downheapBubble(self, index):
        if index < len(self.data):
            leftChild = self.left_child(index)
            rightChild = self.right_child(index)
            if self.data[leftChild][0] < self.data[rightChild][0]:
                child = leftChild
            else:
                child = rightChild

    def min(self):
        print(self.data[0])

    def pqLength(self):
        print(self.length)

    def print_PQ(self):
        print(self.data)
'''

class Priority_Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def parent(self,i):
        return (i - 1) // 2 #why division by 2

    def left_child(self, i):
        return (2 * i) +1

    def right_child(self, i):
        return (2 *i) + 2

    def add_item(self, key, value):
        self.data.append((key, value))
        self.upheapBubble(len(self.data) - 1)
        self.length += 1

    def upheapBubble(self, index):   #store key and value as a tuple
        if index > 0:
            parentIndex = self.parent(index)
            if parentIndex >= 0 and self.data[parentIndex] > self.data[index]:
                self.data[index], self.data[parentIndex] = self.data[parentIndex], self.data[index]#swaps
                self.upheapBubble(parentIndex)
            else:
                return

    def removeMin(self):    # O(1)
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        item = self.data.pop()
        self.downheapBubble(0)
        self.length -= 1
        return item

    def downheapBubble(self, index):
        if index < len(self.data):
            leftChild = self.left_child(index)
            rightChild = self.right_child(index)
            child = leftChild
            if leftChild < len(self.data) and rightChild < len(self.data):
                if self.data[leftChild] < self.data[rightChild]:
                    child = leftChild
                else:
                    child = rightChild
            elif leftChild < len(self.data):
                child = leftChild

            if child < len(self.data) and self.data[index] > self.data[child]:
                self.data[index], self.data[child] = self.data[child], self.data[index]
                self.downheapBubble(child)


    def min(self):
        print(self.data[0])

    def pqLength(self):
        print(self.length)

    def print_PQ(self):
        print(self.data)


pq = Priority_Queue()
pq.add_item(3, 5)
pq.add_item(4, 17)
pq.add_item(2, 7)
pq.add_item(0, 9)

pq.print_PQ()

pq.removeMin()

pq.print_PQ()

pq.min()

pq.pqLength()