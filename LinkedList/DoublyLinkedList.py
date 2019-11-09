class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.next = next
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_element = self.head
        if curr_element is None:
            print("Empty List")
        else:
            while curr_element:
                print(str(curr_element.data), end=" ")
                curr_element = curr_element.next
            print()

    def insert_element_at_front(self, data):
        curr_element = self.head
        new_node = Node(data)
        if curr_element is None:
            self.head = new_node
            return
        else:
            new_node.next = curr_element
            curr_element.prev = new_node
            self.head = new_node

    def insert_element_at_end(self, data):
        curr_node = self.head
        new_node = Node(data)
        if curr_node is None:
            self.head = new_node
            return
        else:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node

    def insert_after_given_node(self, given_node, data):
        curr_node = self.head
        new_node = Node(data)
        if curr_node is None:
            print("Empty List")
            return
        else:
            if given_node.next is None:
                self.insert_element_at_end(data)
                return
            new_node.next = given_node.next
            new_node.prev = given_node
            given_node.next = new_node
            new_node.next.prev = new_node

    def insert_before_given_node(self, given_node, data):
        curr_node = self.head
        new_node = Node(data)
        if curr_node is None:
            print("Empty List")
            return
        else:
            if given_node.prev is None:
                self.insert_element_at_front(data)
                return
            new_node.next = given_node
            new_node.prev = given_node.prev
            given_node.prev = new_node
            new_node.prev.next = new_node

    def insert_at_particular_location(self, location, data):
        new_node = Node(data)
        curr_node = self.head
        count = 1
        if curr_node is None:
            if location != 1:
                print("List is Empty can enter only at 1 location")
                return
            else:
                self.insert_element_at_front(data)
        else:
            while count < location-1 and curr_node.next:
                curr_node = curr_node.next
                count += 1
            self.insert_after_given_node(curr_node, data)

    def delete_first(self):
        curr_node = self.head
        if curr_node is None:
            print("Empty list")
            return
        else:
            curr_node = curr_node.next
            curr_node.prev = None
            self.head = curr_node

    def delete_last(self):
        curr_node = self.head
        if curr_node is None:
            print("Empty List")
            return
        else:
            while curr_node.next:
                temp = curr_node
                curr_node = curr_node.next
            temp.next = None

    def delete_given_node(self, node):
        curr_node = self.head
        if curr_node is None:
            print("Empty List")
            return
        else:
            if node.prev is None:
                self.delete_first()
                return

            if node.next is None:
                self.delete_last()
                return

            node.prev.next = node.next
            node.next.prev = node.prev

    def delete_at_particular_location(self, location):
        curr_node = self.head
        count = 1
        if curr_node is None:
            print("Empty List")
            return
        else:
            while count < location and curr_node.next:
                curr_node = curr_node.next
                count += 1
            self.delete_given_node(curr_node)


dl = DoublyLinkedList()
dl.head = Node(1)
second = Node(2)
third = Node(3)

dl.head.next = second
second.next = third
second.prev = dl.head
third.prev = second
print("Doubly Linked List :", end=" ")
dl.print_list()

dl.insert_element_at_front(0)
print("Doubly Linked List after inserting element at first:", end=" ")
dl.print_list()

dl.insert_element_at_end(4)
print("Doubly Linked List after inserting element at last:", end=" ")
dl.print_list()

dl.insert_after_given_node(second, 40)
print("Doubly Linked List after inserting element after given node:", end=" ")
dl.print_list()

dl.insert_before_given_node(third, 80)
print("Doubly Linked List after inserting element before given node:", end=" ")
dl.print_list()

dl.insert_at_particular_location(5, 100)
print("Doubly Linked List after inserting element after particular location:", end=" ")
dl.print_list()

dl.delete_first()
print("Doubly Linked List after deleting first element:", end=" ")
dl.print_list()

dl.delete_last()
print("Doubly Linked List after deleting last element:", end=" ")
dl.print_list()

dl.delete_given_node(second)
print("Doubly Linked List after deleting given node:", end=" ")
dl.print_list()

dl.delete_at_particular_location(1)
print("Doubly Linked List after deleting at particular location:", end=" ")
dl.print_list()


