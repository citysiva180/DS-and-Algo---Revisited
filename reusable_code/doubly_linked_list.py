class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def print_list(self):

        if self.head is None:
            return "Empty List"
        temp = self.head
        while temp.next is not None:
            print(temp.value)
            temp = temp.next

    def append_items(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop_items(self, value):
        if self.length == 0:
            return "Empty List"
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.tail = self.tail.prev
            self.tail.next = None
            temp.next = None
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
