
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Lqueue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return None
        else:
            temp = self.front
            popped_data = temp.data
            self.front = self.front.next

            if self.front == None:
                self.rear = None

            temp = None
            return popped_data

    def print(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end="->")
                temp = temp.next
            print()


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return None
        else:
            temp = self.top
            popped_data = temp.data
            self.top = self.top.next
            temp = None
            return popped_data

    def printstack(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next


def reverse_stack(s1):
    q1 = Lqueue()

    while not s1.isempty():
        q1.enqueue(node(s1.pop()))

    print("Queue after transferring stack:")
    q1.print()

    while not q1.isempty():
        s1.push(node(q1.dequeue()))

    print("Stack after reversing:")
    s1.printstack()


# Creating Queue
que = Lqueue()

que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))
que.enqueue(node(40))
que.enqueue(node(50))

print("Original Queue:")
que.print()


# Creating Stack
st = stack()

st.push(node(10))
st.push(node(100))
st.push(node(14))
st.push(node(15))
st.push(node(27))

print("\nOriginal Stack:")
st.printstack()


# Reversing Stack using Queue
reverse_stack(st)
