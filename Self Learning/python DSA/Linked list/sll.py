class node :
    def __init__(self,data, next = None):
        self.data = data 
        self.next = next
class linked_list:
    def __init__(self):
        self.head  = None
    def insertatend(self,value ):
        temp = node(value)
        if (self.head != None):
            t1 = self.head 
            while (t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else :
            self.head = temp
    def printll(self):
        t1 = self.head 
        while (t1.next != None):
          print(t1.data)
          t1 = t1.next 
        print(t1.data)
    def insertAtFront(self, value):
        temp = node(value)
        if self.head is None:
           self.head = temp
        else:
            temp.next = self.head
            self.head = temp       
    
ob =linked_list()
ob.insertatend(10)
ob.insertatend(20)
ob.insertAtFront(50)
ob.insertatend(30)
ob.insertAtFront(90)
ob.printll()    