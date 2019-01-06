from tkinter import *
from random import randint


class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def getTree(self):
        return self.root.getBranches()


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def getNodeVal(self):
        return self.value

    def getNodeLeft(self):
        return self.left

    def getNodeRight(self):
        return self.right

    def setNode(self, n):
        if n.value > self.value:
            if self.right is None:
                self.right = n
            else:
                self.right.setNode(n)

        if n.value < self.value:
            if self.left is None:
                self.left = n
            else:
                self.left.setNode(n)

    def getBranches(self):
        if self.right is None:
            print("end of right branch")
        else:
            print("-->" +)


tree = Tree()
numArr = []

for x in range(10):
    numArr.append(randint(1, 101))

for i, val in enumerate(numArr):
    n = Node(val)
    if i == 0:
        tree.setRoot(n)
    else:
        tree.root.setNode(n)

print(numArr)

tree.getTree()
#canvas_width = 600
#canvas_height = 600

#master = Tk()

#w = Canvas(master, width=canvas_width, height=canvas_height)

# w.pack()

# mainloop()
