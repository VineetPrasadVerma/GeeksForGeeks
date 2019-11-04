class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def is_full(self):
        if self.size == self.capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            print("Overflow")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = item
            self.size += 1
            print("Inserted : " + str(item))

    def de_queue(self):
        if self.is_empty():
            print("Underflow")
            return
        else:
            print("Deleted : " + str(self.Q[self.front]))
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

    def get_front(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            return self.Q[self.front]

    def get_rear(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            return self.Q[self.rear]


queue = Queue(3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.is_full())
queue.enqueue(40)
print(queue.is_full())
queue.de_queue()
queue.get_front()
queue.get_rear()
queue.enqueue(10)
queue.get_front()
queue.get_rear()