#Singly linked list
class Node:
    def __init__(self,val):  #init - special constructor
        self.data=val 
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def append(self, new_node):  #everytime i create a new node it has to passed to append
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head #assign temp
            while(temp.next):
                temp=temp.next
            temp.next=new_node #apppending new node
    def insert(self, new_node,pos):   #insert node at first position 
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:           #insert node at a position
            p=1
            while(p!=pos-1 and temp.next!=None):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            return
    
    def print(self):
        temp=self.head
        print("Linked list data:")
        while temp:
            print(temp.data)
            temp=temp.next
    def insert(self, new_node,pos):   #insert node at first position 
        temp = self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            p=1
            while(p!=pos-1 and temp.next!=None):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.n

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.insert(Node(100),1)
list.print()
list.insert(Node(130),4)
list.print()