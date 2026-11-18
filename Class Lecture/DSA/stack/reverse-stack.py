
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


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
        else:
            temp = self.top
            print("Popped Element:", temp.data)
            self.top = self.top.next
            temp = None

    def printstack(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def reverse(self, st1):
        temp = self.top
        while temp:
            st1.push(node(temp.data))
            temp = temp.next


st = stack()
st1 = stack()

st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))
st.push(node(50))

print("Original Stack:")
st.printstack()

st.reverse(st1)

print("Reversed Stack:")
st1.printstack()
