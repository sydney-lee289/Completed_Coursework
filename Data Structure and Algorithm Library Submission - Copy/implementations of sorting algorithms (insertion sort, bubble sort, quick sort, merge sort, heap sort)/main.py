# merge sort
def MergeSort(L):
    if len(L) > 1:
        midIndex = len(L) // 2
        Left = L[:midIndex]
        Right = L[midIndex:]
        L1 = MergeSort(Left)
        R1 = MergeSort(Right)
        result = merge(L1, R1)
        return result
    else:
        return L

def merge(left, right):
    R =[]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            R.append(left[i])
            i+=1
        else:
            R.append(right[j])
            j+=1

    while i < len(left):
        R.append(left[i])
        i+=1
    while j < len(right):
        R.append(right[j])
        j+=1
    return R

# quick sort

def QuickSort(L, low, high):
    if (low < high):
        pIndex = partition(L, low, high)    #pIndex means pivot index
        QuickSort(L, low, pIndex - 1)
        QuickSort(L, pIndex + 1, high )

def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low, high + 1):
        if L[j] <= pivot:
            i+=1
            L[i], L[j] = L[j], L[i]
    return i

# bubble sort

def BubbleSort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


def HeapSort(L):
    pq = Priority_Queue()
    R = []
    for x in L:
        pq.add_item(x)
    count = len(L)
    #print("Add ",pq.data)
    for i in range(count):
        R.append(pq.removeMin())
    return R

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

    def add_item(self, value):
        self.data.append((value))
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
        return self.length

    def print_PQ(self):
        print(self.data)


def InsertionSort(L):
    resultList = []
    for i in range(len(L)):
        bFound = False # did we find an item that is greater than our current item ( i value)
        for j in range(len(resultList)):
            if L[i] < resultList[j]:
                resultList.insert(j, L[i])
                bFound = True
                break
        if(bFound == False):
            resultList.append(L[i])
    return resultList















L1 = [1, 5, 10, -1, 2, 20, 15]
L2 = [1, 5, 10, -1, 2, 20, 15]
L3 = [1, 5, 10, -1, 2, 20, 15]
L4 = [1, 5, 10, -1, 2, 20, 15]
L5 = [1, 5, 10, -1, 2, 20, 15]
L6 = [1, 5, 10, -1, 2, 20, 15]

M1 = [1, 5,10, 15, 20]
M2 = [1, 5,10, 15, 20]
M3 = [1, 5,10, 15, 20]
M4 = [1, 5,10, 15, 20]
M5 = [1, 5,10, 15, 20]
M6 = [1, 5,10, 15, 20]

N1 = [20, 15, 10, 5, 1]
N2 = [20, 15, 10, 5, 1]
N3 = [20, 15, 10, 5, 1]
N4 = [20, 15, 10, 5, 1]
N5 = [20, 15, 10, 5, 1]
N6 = [20, 15, 10, 5, 1]

P1 = [20, 30, 0, 10, 5, 1]
P2 = [20, 30, 0, 10, 5, 1]
P3 = [20, 30, 0, 10, 5, 1]
P4 = [20, 30, 0, 10, 5, 1]
P5 = [20, 30, 0, 10, 5, 1]
P6 = [20, 30, 0, 10, 5, 1]



'''
print('unsorted (input list): ', L1)
print('merge sort: ', MergeSort(L2))
QuickSort(L3, 0, len(L3) - 1)
print('quick sort: ', L3)
BubbleSort(L4)
print('bubble sort: ', L4)
R1=InsertionSort(L5)
print('insertion sort: ', R1)
T1 = HeapSort(L6)
print('heap sort: ', T1)

print()

print('unsorted (input list): ', M1)
print('merge sort: ', MergeSort(M2))
QuickSort(M3, 0, len(M3) - 1)
print('quick sort: ', M3)
BubbleSort(M4)
print('bubble sort: ', M4)
R2 = InsertionSort(M5)
print('insertion sort: ', R2)
T2 = HeapSort(M6)
print('heap sort: ', T2)

print()

print('unsorted (input list): ', N1)
print('merge sort: ', MergeSort(N2))
QuickSort(N3, 0, len(N3) - 1)
print('quick sort: ', N3)
BubbleSort(N4)
print('bubble sort: ', N4)
R3 = InsertionSort(N5)
print('insertion sort: ', R3)
T3 = HeapSort(N6)
print('heap sort: ', T3)

print()

print('unsorted (input list): ', P1)
print('merge sort: ', MergeSort(P2))
QuickSort(P3, 0, len(P3) - 1)
print('quick sort: ', P3)
BubbleSort(P4)
print('bubble sort: ', P4)
R4 = InsertionSort(P5)
print('insertion sort: ', R4)
T4 = HeapSort(P6)
print('heap sort: ', T4)
'''

print('Homework Format')

print()

print('Merge Sort:')
print('input: ', L1, 'output: ', MergeSort(L2))
print('input: ', M1, 'output: ', MergeSort(M2))
print('input: ', N1, 'output: ', MergeSort(N2))
print('input: ', P1,  'output: ', MergeSort(P2))

print()

print('Quick Sort:')
QuickSort(L3, 0, len(L3) - 1)
print('input: ', L1, 'output: ', L3)
QuickSort(M3, 0, len(M3) - 1)
print('input: ', M1, 'output: ', M3)
QuickSort(N3, 0, len(N3) - 1)
print('input: ', N1, 'output: ', N3)
QuickSort(P3, 0, len(P3) - 1)
print('input: ', P1, 'output: ', P3)

print()

print('Bubble Sort:')
BubbleSort(L4)
print('input: ', L1, 'output: ', L4)
BubbleSort(M4)
print('input: ', M1, 'output: ', M4)
BubbleSort(N4)
print('input: ', N1, 'output: ', N4)
BubbleSort(P4)
print('input: ', P1, 'output: ', P4)

print()

print('Insertion Sort:')
R1=InsertionSort(L5)
print('input: ', L1, 'output: ', R1)
R2=InsertionSort(M5)
print('input: ', M1, 'output: ', R2)
R3=InsertionSort(N5)
print('input: ', N1, 'output: ', R3)
R4=InsertionSort(P5)
print('input: ', P1, 'output: ', R4)

print()

print('Heap Sort:')
T1 = HeapSort(L6)
print('input: ', L1, 'output: ', T1)
T2 = HeapSort(M6)
print('input: ', M1, 'output: ', T2)
T3 = HeapSort(N6)
print('input: ', N1, 'output: ', T3)
T4 = HeapSort(P6)
print('input: ', P1,'output: ', T4)

print()