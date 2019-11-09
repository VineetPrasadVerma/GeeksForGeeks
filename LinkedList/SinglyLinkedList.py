class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_element = Node(data)
        curr_element = self.head
        if curr_element is None:
            self.head = new_element
            return
        else:
            new_element.next = curr_element
            self.head = new_element

    def insert_at_end(self, data):
        new_element = Node(data)
        curr_element = self.head
        if curr_element is None:
            self.head = new_element
            return
        # else:
        # while curr_element.next:
        # curr_element = curr_element.next
        # curr_element.next = new_element
        else:
            while curr_element:
                temp = curr_element
                curr_element = curr_element.next
                temp.next = new_element

    def insert_at_given_node(self, data, location):
        new_node = Node(data)
        curr_node = self.head
        count = 1
        if curr_node is None:
            if location != 1:
                return "You are mad"
            else:
                self.insert_at_front(data)
        else:
            while count < location - 1 and curr_node.next:
                curr_node = curr_node.next
                count += 1
                new_node.next = curr_node.next
                curr_node.next = new_node

    def delete_front(self):
        curr_node = self.head
        if curr_node is None:
            print("Empty List")
            return
        else:
            curr_node = curr_node.next
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
                temp.next = curr_node.next

    def delete_at_given_position(self, location):
        curr_node = self.head
        count = 1
        if curr_node is None:
            print("Empty list")
            return
        else:
            while count != location and curr_node.next:
                temp = curr_node
                curr_node = curr_node.next
                count += 1
                temp.next = curr_node.next

    def delete_by_key(self, key):
        curr_node = self.head
        if curr_node is Node:
            print("Empty List")
            return
        else:
            while curr_node.data != key:
                temp = curr_node
                if curr_node.next is None:
                    print("Key not found")
                    return
                curr_node = curr_node.next
                temp.next = curr_node.next

    def print_list(self):
        curr_element = self.head
        if curr_element is None:
            print("Empty List")
        else:
            while curr_element:
                print(curr_element.data, end="")
                curr_element = curr_element.next

