class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 1

    def print_list(self):
        temp = self.head
        if temp.next is not None:
            print(temp.value)
            temp = temp.next
        else:
            print("Empty List")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return "Empty List"
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return "Empty List"
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return "Unbound Index"
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            for _ in range(self.length-1, index, -1):
                temp = temp.next
        return temp

    def set_items(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return "Unbound Index"
        if index == 0:
            return self.prepend(self, value)
        if index == self.length:
            return self.append(self, value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after

        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
