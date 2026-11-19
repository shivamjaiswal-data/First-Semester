class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self):  # Recursive
        self._inorder(self.root)
        print()

    def _inorder(self, temp):
        if temp is None:
            return
        self._inorder(temp.left)
        print(temp.data, end=" ")
        self._inorder(temp.right)


btree = BST()
btree.insert(node(10))
btree.insert(node(20))
btree.insert(node(3))
btree.insert(node(17))
btree.insert(node(40))
btree.inorder()