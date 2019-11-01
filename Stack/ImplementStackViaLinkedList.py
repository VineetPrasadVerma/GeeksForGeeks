class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def push(self, data):
        if self.head is None:
            self.head = StackNode(data)
        else:
            new_node = StackNode(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return "Empty Stack"
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    def peek(self):
        if self.head is None:
            return "Empty stack"
        else:
            return self.head.data


stack = Stack()
print(stack.pop())
print(stack.peek())
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.peek())
print(stack.pop())
print(stack.peek())
