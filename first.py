from tkinter import *
from random import randint

canvas_width = 600
canvas_height = 600
numArr = []
nodeSize = 60
textSize = 30

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="red")

canvas.pack()


class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node
        node.printNode(True)

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
            print("-->" + str(self.right.value))
            self.right.getBranches()

        if self.left is None:
            print("end of left branch")
        else:
            print(str(self.left.value) + "<--")
            self.left.getBranches()


    def printNode(self, isRoot):
        if isRoot:
            print("print root node")
            x1 = canvas_width / 2 - nodeSize / 2
            y1 = 10
            x2 = canvas_width / 2 + nodeSize / 2
            y2 = nodeSize
            canvas.create_oval(x1, y1, x2, y2) # x1, y1, x2, y2, options
            canvas.create_text(x1 + nodeSize / 2, (y2 - y1) / 2 + y1 , text=str(self.value))

tree = Tree()

for x in range(10):
    numArr.append(randint(1, 101))

for i, val in enumerate(numArr):
    n = Node(val)
    if i == 0:
        tree.setRoot(n)
    else:
        tree.root.setNode(n)



tree.getTree()
mainloop()
