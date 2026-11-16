class node :
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class ll:
    def __init__(self ,head = None):
        self.head = head


    def insertatend(self,value):
        temp = node(value)
       
        if (self.head != None):
            t1 = self.head 
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
         
         
    def printll(self):
         t1 = self.head 
         while (t1.next != None):
                 print(t1.data)
                 t1 = t1.next
         print(t1.data)
ob = ll()
ob.insertatend(45)
ob.insertatend(46)
ob.insertatend(47)
ob.printll()
