class Node:
    def __init__(self, val):
        self.parent = None
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, parentNode, newNode):
        if self.root == None:
            self.root = newNode
        elif parentNode.left == None:
            parentNode.left = newNode
            newNode.parent = parentNode
        elif parentNode.right == None:
            parentNode.right = newNode
            newNode.parent = parentNode
        else:
            print("error")

    def originalRemove(self, node): #in office hrs 3.17.2023, you said we could keep the children/subtrees as in the lab implementation
        if node.left == None and node.right == None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left != None and node.right != None:
            print("error")
        else:
            childNode = None
            if node.left != None:
                child = node.left
            else:
                child = node.right
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
                child.parent = node.parent

    def remove(self, node):
        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    def depth(self, node):
        if node == self.root:
            return 0
        else:
            return 1 + self.depth(node.parent)

    def height(self, node):
        if node == None:
            return 0
        else:
            x = self.height(node.left)
            y = self.height(node.right)
            return max(x+1, y+1)
    def printInOrder(self, node):
        if node != None:
            self.printInOrder(node.left)
            print(node.value)
            self.printInOrder(node.right)

    def printPreOrder(self, node):
        if node != None:
            print(node.value)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if node != None:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.value)

    def print(self, node): # print level by level
        node_list = []
        print(self.root.value, end = ' ')
        if self.root.left != None:
            node_list.append(self.root.left)
        if self.root.right != None:
            node_list.append(self.root.right)
        while len(node_list) != 0:
            node = node_list.pop(0)
            print(node.value, end = ' ')
            if node.left != None:
                node_list.append(node.left)
            if node.right != None:
                node_list.append(node.right)

        print()


    def sumOfNodesLevelbyLevel(self):
        node_list = []
        D = dict()
        node_list.append((self.root, 0))
        while len(node_list) != 0:
            item = node_list.pop(0)
            node = item[0]
            level = item[1]
            if node.left != None:
                node_list.append((node.left, level + 1))
            if node.right != None:
                node_list.append((node.right, level + 1))
            if level not in D.keys():
                D[level] = node.value
            else:
                D[level] = D[level] + node.value
        R = []
        for key in D.keys():
            R.append(D[key])
        return R




# Homework Output

bt = BinaryTree()
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)
G = Node(7)
H = Node(8)
I = Node(9)
J = Node(10)
K = Node(11)
L = Node(12)
M = Node(13)
N = Node(14)



bt.insert(None, A)
bt.insert(A, B)
bt.insert(A, C)
bt.insert(B, D)
bt.insert(B, E)
bt.insert(C, F)
bt.insert(C, G)
bt.insert(D, H)
bt.insert(D, I)
bt.insert(E, J)
bt.insert(G, K)
bt.insert(I, L)
bt.insert(I, M)
bt.insert(K, N)

bt.print(A)
print(bt.sumOfNodesLevelbyLevel())
'''
(for in class demo to see if it works)
A = (0, 1)
x,y = A

print(x,y)
'''