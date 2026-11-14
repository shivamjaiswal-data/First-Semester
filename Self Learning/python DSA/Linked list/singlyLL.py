class Node :
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class SinglyLinkedList():
    def __init__(self,head =None):
        self.head = head 


    def InsertAtend(self,value):
        temp = Node(value)
        if(self.head != None ):
            t1 = self.head 
            while(t1.next != None):
                t1 = t1.next 
            t1.next= temp 
        else:
            self.head  =  temp 
    def printLL(self):
         t1 = self.head 
         while(t1.next != None):
            print(t1.data)
            t1 = t1.next 
         print(t1.data)
ob = SinglyLinkedList()
ob.InsertAtend(12)
ob.InsertAtend(13)
ob.printLL()