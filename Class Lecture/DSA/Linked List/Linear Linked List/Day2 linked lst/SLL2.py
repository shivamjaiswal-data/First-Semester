#Singly Linear list

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =None
    # def append(self, new_node):
        # self.head = new_head.
    def insert(self, new_node,pos):
        # if pos==1:
        #    new_node.next=self.head #inserting at first position 
        #    self.head =new_node 
        # else:
           p =1
           while(p!=pos-1 or temp != None):
               temp = temp.next 
               p+=1
           new_node.next=temp.next
           temp.next=new_node
           
          
    def print(self):
        count=0
        
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next.next
        
            
        print(sum)
list = LinkedList()
n1=Node(10)
n2 =Node(20)
n3=Node(30)
# list.append(n1)
# list.append(n2)
# list.append(n3)
list.append(Node(40))
list.append(Node(55))
list.print()
#How to count Node of Linked List
# How to get total sum Nodes

                
