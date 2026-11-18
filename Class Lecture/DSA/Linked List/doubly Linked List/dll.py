class node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
class linked_list :
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp =self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else: #First Node
            self.head = new_node
    def print(self):
        temp = self.head
        print("List Element")
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
    # def print(self):
    #     temp =self.head
    #     print("List Element:")
list = linked_list()
list.append(node(12))
list.append(node(16))
list.print()

