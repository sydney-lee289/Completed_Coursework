class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, newNode):   #O(n)
        if index == 0:
            if self.size == 0:
                self.head = newNode
                self.size +=1
            else:
                newNode.next = self.head
                self.head = newNode
                self.size += 1
        elif index <= self.size:
            i = 0
            temp = self.head
            while i < index - 1:
                temp = temp.next
                i += 1
            newNode.next = temp.next
            temp.next = newNode

    def remove(self, index): #O(n)
        if index == 0:
            self.head = self.head.next
        else:
            i = 0
            temp = self.head
            while i < index - 1:
                temp = temp.next
                i += 1
            temp.next = temp.next.next

    def printSingleLinkedList(self): #O(n)
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next


myLinkedList = SingleLinkedList()
myLinkedList.insert(0, Node(5))
myLinkedList.insert(1, Node(5))
myLinkedList.remove(1)
myLinkedList.printSingleLinkedList()

