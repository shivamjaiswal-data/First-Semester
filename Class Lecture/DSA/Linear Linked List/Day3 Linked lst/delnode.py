#Singly Linear list

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =None
    def append(self, new_node):
        if (self.head == None):
           self.head =new_node 
        else:
           temp = self.head
           while(temp.next):
               temp = temp.next
           temp.next =new_node
    
    def del_node(self, value):
        temp = self.head
        #deleting first node
        if temp.data==value:
            self.head=self.head.next
            return
        while(temp):
            if temp.data==value:
                break
            else:
                prev=temp
                temp=temp.next
            if temp==None:
                print("Value is not there in the list")
            prev.next=temp.next
            temp=None
        
            
        
list = LinkedList()
n1=Node(10)
n2 =Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(55))





                
