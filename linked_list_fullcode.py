class Node:
    def __init__(self, value):

        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):

        if self.head is None:
            return "Empty List"
        else:
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
            self.head.next = new_node
            self.head = new_node
        return True

    def prepend_items(self,value):
        new_node = Node(value)
        