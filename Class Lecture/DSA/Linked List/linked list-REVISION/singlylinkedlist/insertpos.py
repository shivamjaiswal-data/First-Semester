class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
       self.head=None

    def append(self,new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            p=1
            while p!=pos-1 and temp.next!=None:
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            return

    def del_node(self,value):
        temp=self.head
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
                    print("Value is not in the list")
                    return 
        prev.next=temp.next #
        temp=None

    def reverse(self):
        prev=None
        temp=self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def mid_node(self):
                temp=temp1=self.head
                prev=None
                while temp1 and temp1.next:
                    prev=temp
                    temp=temp.next
                    temp1=temp1.next.next
                print("Middle node:",temp.data)
                prev.next=temp.next
                temp=None

    def delfirst_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None

    def print(self):
        
        temp=self.head
        print("Linked list data")
        while temp:
            print(temp.data)
            temp=temp.next

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(50)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.print()
print("List after insertion")
list.insert(Node(100),3)
list.insert(Node(70),4)
list.print()
print("Middle node:")
list.mid_node()
list.delfirst_last()
# list.print()
#list.del_node(100)
#print("Linked list after deleting")
#list.print()
#print("Reversed list")
#list.reverse()
#list.print()