class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear == self.front - 1) or (self.rear == self.size - 1 and self.front == 0):
            print("Queue is full")
        else:
            if self.rear == -1:
                self.rear = 0
                self.front = 0
            elif self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            return "Queue is Empty"
        else:
            temp = self.queue[self.front]
            if self.front == self.rear:
                temp = self.queue[self.front]
                self.front = -1
                self.rear = -1
            elif self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
            return temp


    def display(self):
        if self.front == -1:
            print("Empty Queue")

        else:
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
                print()
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i], end=" ")
                for j in range(0, self.rear + 1):
                    print(self.queue[j], end=" ")
        print()


ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
