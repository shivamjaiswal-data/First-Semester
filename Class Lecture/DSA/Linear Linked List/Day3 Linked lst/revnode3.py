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
            return
        prev.next=temp.next
        temp=None

    def reverse(self):
        curr = self.head
        prev = None
        while(curr):
            nextnode= curr.next
            curr.next =prev
            prev = curr
            curr =nextnode
        return prev

list = LinkedList()
n1=Node(10)
n2 =Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(55))
list.reverse()  


temp=list.head
while(temp):
    print(temp.data)
    temp=temp.next
#give me a code of sum of two consecutive nodes in linked list and return the new linked list
def sum_consecutive_nodes(self):
    if self.head is None or self.head.next is None:
        return self.head  # Return the original list if it has 0 or 1 node

    new_list = LinkedList()
    current = self.head

    while current and current.next:
        sum_value = current.data + current.next.data
        new_node = Node(sum_value)
        new_list.append(new_node)
        current = current.next.next  # Move to the next pair of nodes

    # If there's an odd node left, append it as is
    if current:
        new_list.append(Node(current.data))

    return new_list