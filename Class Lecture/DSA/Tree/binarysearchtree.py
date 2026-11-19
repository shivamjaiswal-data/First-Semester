class node : 
    def __init__(self,value):
        self.right = None
class BST:
    def __init__(self):
        self.root =None
    def insert (self,new_node):
        if self.root is None: 
            self.root = new_node
            return
        temp = self.root
        while True :
            if new_node.data < temp.data:
                temp



    def inorder(self):# Recursive
        if self.root is None :
            return 
        else:
            self.inorder(self.left)
            print(self.data,end = " ")
            self.inorder(self.right)



btree = BST()
btree.insert(node(10))
btree.insert(node(20))
btree.insert(node(3))
btree.insert(node(17))
btree.insert(node(40))
btree.iinorder()



