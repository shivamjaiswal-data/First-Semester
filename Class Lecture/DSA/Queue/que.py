class node :
    def __init__ (self,val):
        self.data  = val
        self.next = None
class Lqueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next =  new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self ):
        temp = self.front
        print("Deleted Node :" , temp.data)
        self.front =self.front.next
        temp = None
        if self.front == None:
            self.rear == None
    def  print(self):
        temp = self.front
        while temp:
            print(temp.data,end = "->")
            temp = temp.next
        print()
que =Lqueue()
que.enqueue(node(10))
que.enqueue(node(20))

que.print()