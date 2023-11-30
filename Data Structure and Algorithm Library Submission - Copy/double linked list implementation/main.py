# just to see if it updates!!!

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insertAt(self, index, newNode):
        if index == 0:
            if self.len == 0:
                self.head = newNode
                self.tail = newNode
            elif self.len != 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
        elif index == self.len:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            temp = self.head
            i = 0
            while i < index - 1:
                temp = temp.next
                i += 1
                
            newNode.next = temp.next
            temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp
        self.len += 1

    def remove(self, index):
        if self.len == 1:
            self.head = None
            self.tail = None
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.len - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            i = 0
            while i < index - 1:
                temp = temp.next
                i += 1
            temp.next = temp.next.next
            if temp.next != None:
                temp.next.prev = temp

    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.val)
            temp = temp.next

    def reverse(self):
        temp = self.head
        while(temp != None):
            temp.next,temp.prev = temp.prev, temp.next
            if (temp.prev == None):
                self.head = temp
            temp = temp.prev

    def swap(self, index1, index2):
        index = 0
        temp1 = self.head
        while(index < index1):
            temp1 = temp1.next
            index += 1
        temp2 = self.head
        while(index < index2):
            temp2 = temp2.next
            index += 1
        temp1.val,temp2.val = temp2.val,temp1.val

# HOMEWORK OUTPUT
dLList = DoubleLinkedList()
dLList.insertAt(0, Node(1))
dLList.insertAt(1, Node(3))
dLList.insertAt(2, Node(5))
dLList.insertAt(2, Node(2))
dLList.insertAt(0, Node(0))
dLList.insertAt(4, Node(4))
print("First Print Results\n")
dLList.print()
dLList.reverse()
print("Second Print Results\n")
dLList.print()
dLList.swap(0, 5)
dLList.swap(1, 4)
print("Third Print Results\n")
dLList.print()
dLList.remove(0)
dLList.remove(4)
dLList.remove(1)
print("Fourth Print Results\n")
dLList.print()

