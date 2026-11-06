
# Node Class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Queue Class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Enqueue Operation
    def enqueue(self, data):
        temp = Node(data)

        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    # 2. Dequeue Operation
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Dequeued Element:", temp.data)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 3. Display Operation
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Queue Contains...")
            temp = self.front

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


# Creating Queue
q1 = Queue()

# Enqueue Elements
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

# Display Queue
print("Original Queue:")
q1.display()

# Dequeue Operation
print("\nAfter Dequeue:")
q1.dequeue()

# Display Updated Queu
q1.display()
