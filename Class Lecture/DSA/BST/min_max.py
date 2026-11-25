#find minimun node and maximun node of BST
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.lcnt = 0

    def insert(self,newNode):
        if self.root == None:
            self.root = newNode
            return
        else:
            temp = self.root
            while True:
                if newNode.data < temp.data:    #left subtree
                    if temp.left is None:
                        temp.left = newNode
                        return
                    else:
                        temp = temp.left
                else:                   #right subtree
                    if temp.right is None:
                        temp.right = newNode
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is not None or rt.right is None:
                self.lcnt += 1
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            self.lcnt += 1
            print(rt.data, end=" ")

    def find_minmax(self,rt):
        temp = rt
        while temp.left:
            temp = temp.left
        print("\nMin value:",temp.data)
        temp = rt
        while temp.right:
            temp = temp.right
        print("Max value:",temp.data)
    
btree = BST()
btree.insert(Node(100))
btree.insert(Node(10))
btree.insert(Node(450))
btree.insert(Node(4))
btree.insert(Node(65))
btree.insert(Node(300))
btree.insert(Node(500))
btree.insert(Node(50))
print("\nInorder")
btree.inorder(btree.root)
print("\nNo of nodes(post-order): ",btree.lcnt)
print("\nPre-order")
btree.preorder(btree.root)
print("\nPost-order")
btree.postorder(btree.root)
btree.find_minmax(btree.root)