
# Singly Linear list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1 and temp != None:
                temp = temp.next
                p += 1
            if temp == None:
                print("Invalid position")
            else:
                new_node.next = temp.next
                temp.next = new_node

    def print(self):

        count = 0
        temp = self.head

        while temp != None:
            print(temp.data)
            count += 1
            temp = temp.next

        print("Total Nodes:", count)

    def sum(self):

        total = 0
        temp = self.head

        while temp != None:
            total = total + temp.data
            temp = temp.next

        print("Total Sum:", total)


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(Node(40))
list.append(Node(55))

list.insert(Node(50), 2)

list.print()
list.sum()
