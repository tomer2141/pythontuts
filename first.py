from tkinter import *
from random import randint

canvas_width = 600
canvas_height = 600
numArr = []
nodeSize = 60
textSize = 30
lineSpace = 70

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="red")

canvas.pack()


class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def getTree(self):
        return self.root.getBranches()

    def printTree(self):
        self.root.printNode("root", None)


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None

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

    def printNode(self, type, parent):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        if type == "root":
            print("print root node")
            x1 = int(canvas_width / 2 - nodeSize / 2)
            y1 = int(10)
            x2 = int(canvas_width / 2 + nodeSize / 2)
            y2 = int(nodeSize)
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
        elif type == "right":
            x1 = int(parent.x2 + nodeSize / 2)
            x2 = int(x1 + nodeSize)
            y1 = int(parent.y2 + lineSpace)
            y2 = int(y1 + nodeSize)
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            # handle right
        elif type == "left":
            print("left node" + str(self.value))
            x1 = int(parent.x1 - nodeSize)
            x2 = int(x1 + nodeSize)
            y1 = int(parent.y2 + lineSpace)
            y2 = int(y1 + nodeSize)
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            # handle left

        canvas.create_oval(x1, y1, x2, y2)  # x1, y1, x2, y2, options
        canvas.create_text(x1 + nodeSize / 2, (y2 - y1)
                           / 2 + y1, text=str(self.value))
        if self.right is not None:
            self.right.printNode("right", self)

        if self.left is not None:
            self.left.printNode("left", self)


tree = Tree()

for x in range(10):
    numArr.append(randint(1, 101))

for i, val in enumerate(numArr):
    n = Node(val)
    if i == 0:
        tree.setRoot(n)
    else:
        tree.root.setNode(n)

print(numArr)
tree.printTree()

mainloop()
