from random import randrange


class Hashtable:
    def __init__(self, n):           # ((ai +b) % P) % N
        self.table = [None] * n
        self.P = 1093345121
        self.a = 1 + randrange(self.P - 1)
        self.b = randrange(self.P)
        self.N = n
        self.len = 0


    def hashfunction(self, key):
        return((hash(key) * self.a + self.b) % self.P) % self.N

    def setItem(self, key, value):
        index = self.hashfunction(key)
        if self.table[index] == None:
            self.table[index] = (key, value)
        elif type(self.table[index]) is tuple:     # tuple is immutable in python
            if self.table[index][0] == key:
                self.table[index] = (key, value)
            else:
                temp = []
                temp.append(self.table[index])
                temp.append((key, value))
                self.table[index] = temp
        else: # a list
            bPresent = False
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    bPresent = True

            if (bPresent == False):
                self.table[index].append((key, value))
        self.len += 1

    def getItem(self, key):
        index = self.hashfunction(key)
        if self.table[index] == None:
            return None
        elif type(self.table[index]) is tuple:
            if self.table[index][0] == key:
                return self.table[index][1]
        else:
            value = None
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    value = self.table[index][i][1]
                    break
            return value

    def removeItem(self, key):
        index = self.hashfunction(key)
        if self.table[index] is None:
            return
        elif type (self.table[index]) == 'tuple':
            self.table[index] = None
        else:
            temp = -1
            for i in range(len(self.table[index])):
                if key == self.table[index][i][0]:    #the first item in the tuple
                    temp = i
                    break
            if temp != -1:
                self.table[index].pop(temp)

        self.len -= 1

    def length(self):
        return self.len
    
    def printHashtable(self):
        print(self.table)

# Main Program

ht = Hashtable(7)
ht.setItem('A', 100)
ht.setItem('A', 200)
print(ht.getItem('A'))
ht.setItem('B', 300)
ht.setItem('C', 400)
ht.setItem('D', 500)
ht.setItem('E', 600)
ht.setItem('E', 700)
ht.setItem('F', 800)
ht.setItem('G', 900)
ht.setItem('H', 1000)
ht.setItem('I', 1100)
ht.setItem('J', 1200)
ht.setItem('J', 1300)
ht.setItem('K', 1400)
ht.setItem('L', 1500)
ht.setItem('M', 1600)
ht.setItem('N', 1700)
ht.setItem('O', 1800)

print(ht.getItem('O'))

ht.printHashtable()
print(ht.length())
ht.removeItem('B')
ht.printHashtable()
print(ht.length())
ht.removeItem('A')
ht.printHashtable()
print(ht.length())