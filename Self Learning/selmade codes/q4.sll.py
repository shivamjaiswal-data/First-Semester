class node :
    def __init__ (self,val):
        self.data = val 
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def append (self,values ):
        temp = values
        if self.head ==None:
            self.head  =  temp 
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next  = temp
    def printll(self):
        while self.head :
            print(self.head.data, end = "-->")
            self.head = self.head.next
obj = SLL()
obj.append(node(10))
obj.append(node(20))
obj.append(node(30))

obj.printll()
    

