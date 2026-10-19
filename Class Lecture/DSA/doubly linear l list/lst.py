#Doubly linear linked list
class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        temp = self.head
        if temp:
            while temp.next:    #finding last node
                temp = temp.next
            temp.next = new_node    #append
            new_node.prev = temp
        else:   #First node
            self.head = new_node

    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            while(p!=pos-1 and temp.next):
                temp = temp.next
                p+=1
            #temp.next = new_node
            #new_node.prev = temp
            new_node.next = temp.next
            if temp.next:           #for last position
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def rev(self):
        temp = self.head
        print("\nReverse list")
        while temp.next:
            temp = temp.next
        while(temp):
            print(temp.data,end = " ")
            temp = temp.prev

    def del_node(self,value):
            temp=self.head
            if temp.data==value:  #first node to delete
                self.head=self.head.next
                self.head.prev = None
            else:
                while(temp.data!= value and temp):
                    temp = temp.next
                    if temp == None:
                        print("Value is not present in list")
                        return
                temp.prev.next = temp.next
                if temp.next:  #if not last node
                    temp.next.prev = temp.prev
                temp = None

    def count_occ(self,num):
        temp = self.head
        cnt = 0
        while temp :
            if temp.data == num:
                cnt+=1
            temp = temp.next
        print("the ocuurance" , cnt)
    def print(self):
        temp = self.head
        print("\nList elements: ")
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
    def swap(self):
        temp =  node1 = self.head # index is first node
        while  temp.next : # tmep is the laste node
            temp = temp.next 
        temp.next  = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev = None
        self.head   = temp
        

list=LinkedList()
list.append(Node(12))
list.append(Node(52))
list.append(Node(22))
list.print()
list.insert(Node(37),1)
list.print()
#list.rev()
#list.print()

