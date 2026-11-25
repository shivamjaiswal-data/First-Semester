
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

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

    def inorder(self,temp):          #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)

btree = BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
btree.inorder(btree.root)