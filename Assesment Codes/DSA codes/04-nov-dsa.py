
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        temp = Node(new_node)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            temp = self.top
            print('Popped Element :-', temp.data)
            self.top = self.top.next
            temp = None

    def print(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            print('Stack Contains...')
            temp = self.top

            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next

            print('Null')


# Creating Stack
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.print()

print('After a Pop Operation :- ')
s.pop()
s.print()

