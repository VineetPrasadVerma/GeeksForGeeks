class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def print_list(self):
        if self.last is None:
            print("Empty List")
            return
        else:
            curr_node = self.last.next
            while curr_node:
                print(curr_node.data, end=" ")
                curr_node = curr_node.next
                if curr_node == self.last.next:
                    print()
                    break

    def insert_at_empty(self, data):
        if self.last is not None:
            print("List is not Empty use another method")
            return
        else:
            new_node = Node(data)
            self.last = new_node
            new_node.next = new_node

    def insert_at_front(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node = Node(data)
            self.last = new_node
            new_node.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node = Node(data)
            self.last = new_node
            new_node.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def insert_after_given_item(self, data, item):
        if self.last is None:
            print("Empty List")
            return
        else:
            new_node = Node(data)
            curr_node = self.last.next
            while curr_node:
                if curr_node.data == item:
                    new_node.next = curr_node.next
                    curr_node.next = new_node

                    if curr_node == self.last:
                        self.last = new_node
                        return
                    else:
                        return
                curr_node = curr_node.next
                if curr_node == self.last.next:
                    print("Item not found")
                    break

    def insert_after_given_location(self, data, location):
        count = 1
        if self.last is None:
            if location != 1:
                print("List is empty can;t insert at this location")
            else:
                self.insert_at_front(data)
        else:
            curr_node = self.last.next
            while count < location - 1 and curr_node.next != self.last.next:
                count += 1
                curr_node = curr_node.next
            self.insert_after_given_item(data, curr_node.data)

    def delete_first(self):
        if self.last is None:
            print("Empty list")
            return
        else:
            curr_node = self.last.next
            if curr_node == self.last:
                self.last = None
                return
            self.last.next = curr_node.next

    def delete_last(self):
        if self.last is None:
            print("Empty List")
            return
        else:
            curr_node = self.last.next
            if curr_node == self.last:
                self.last = None
                return
            while curr_node.next != self.last.next:
                temp = curr_node
                curr_node = curr_node.next
            temp.next = self.last.next

    def delete_by_given_key(self, key):
        if self.last is None:
            print("Empty List")
            return
        else:
            curr_node = self.last.next
            while curr_node.data != key:
                if curr_node.next == self.last.next:
                    print("Item not found")
                    return
                temp = curr_node
                curr_node = curr_node.next

            if curr_node == self.last:
                self.last = None
                return

            if curr_node == self.last.next  :
                self.delete_first()
                return

            temp.next = curr_node.next


cll = CircularLinkedList()
print("Empty List :", end=" ")
cll.print_list()

cll.insert_at_front(0)
print("Circular Linked List after inserting at front:", end=" ")
cll.print_list()

first = Node(1)
second = Node(2)
cll.last = Node(3)
first.next = second
second.next = cll.last
cll.last.next = first
print("Circular Linked List :", end=" ")
cll.print_list()

cll.insert_at_front(0)
print("Circular Linked List after inserting at front:", end=" ")
cll.print_list()

cll.insert_at_end(10)
print("Circular Linked List after inserting at end:", end=" ")
cll.print_list()

cll.insert_after_given_item(60, 2)
print("Circular Linked List after inserting at given node:", end=" ")
cll.print_list()

cll.insert_after_given_item(50, -1)
print("Circular Linked List after inserting at given node:", end=" ")
cll.print_list()

cll.insert_after_given_location(100, 4)
print("Circular Linked List after inserting at given location:", end=" ")
cll.print_list()

cll.delete_first()
print("Circular Linked List after deleting first node:", end=" ")
cll.print_list()

cll.delete_last()
print("Circular Linked List after deleting last node:", end=" ")
cll.print_list()

cll.delete_by_given_key(1)
print("Circular Linked List after deleting given key:", end=" ")
cll.print_list()

cll.delete_by_given_key(2)
print("Circular Linked List after deleting given key:", end=" ")
cll.print_list()

