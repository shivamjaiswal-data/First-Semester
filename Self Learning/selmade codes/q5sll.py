# class node :
#     def __init__(self,val):
#         self.data = val
#         self.next = None
# class SLL:
#     def __init__(self):
#         self.head = None
#     def appendlist(self,node):
#         t1 = self.head
#         if self.head == None:
#            self.head = node
#         else:
#             while t1 != None :
#                 t1= t1.next
#             t1 = node
#     def printll(self):
#         temp = self.head 
#         print(self.head.next)

# obj = SLL()
# obj.appendlist(node(10))
# obj.appendlist(node(20))
# obj.appendlist(node(30))
# obj.printll()
            












class Node :

    def __init__(self,data):
        self.data = data
        self.next = None
        pass


class Sll:

    def __init__(self):
        self.head = None
        pass


    def addNode(self,newNode):

        if self.head == None :
            self.head = newNode
            return self.head

        copyOfHead = self.head

        if  copyOfHead.next == None :
                   print("NOde is EMpty")
                   return

        while copyOfHead != None :
            copyOfHead = copyOfHead.next

        copyOfHead.next = newNode

        return self.head

    def printNode(self):

       

        copyNode = self.head

        while copyNode != None :
            print(copyNode.data, end="-->")
            copyNode = copyNode.next
        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
sll1 = Sll()

sll1.addNode(node1)
sll1.addNode(node2)
sll1.addNode(node3)
sll1.addNode(node4)
sll1.addNode(node5)
sll1.addNode(node6)
sll1.addNode(node7)
sll1.addNode(node8)
sll1.addNode(node9)

sll1.printNode()



        




















