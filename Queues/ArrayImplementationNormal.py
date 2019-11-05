class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.size = 0
        self.rear = 0
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
        if self.size <= self.capacity:
            self.Q[self.rear] = item
            print("Inserted : " + str(item))
            self.rear += 1
            self.size += 1
        else:
            return "Overflow"

    def de_queue(self):
        if self.size == 0:
            return "Underflow"
        else:
            print("Deleted : " + str(self.Q[self.front]))
            self.front += 1
            self.size -= 1

    def get_front(self):
        if self.is_empty():
            return "Empty"
        else:
            print(self.Q[self.front])

    def get_rear(self):
        if self.is_empty():
            return "Empty"
        else:
            print(self.Q[self.rear - 1])


queue = Queue(30)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.de_queue()
queue.get_front()
queue.get_rear()
queue.enqueue(10)
queue.get_front()
queue.get_rear()
