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
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_items(self):
        if self.head is None:
            return False
        prev = self.head
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True

    def pop_first(self):
        if self.head is None:
            return False
        temp, self.head = self.head, temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True

    def get(self, index):
        if index not in range(self.length):
            return "Unbound Node"
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_items(self, index, value):
        if index not in range(self.length):
            return "Unbound Node"
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index not in range(self.length):
            return "Unbound Node"
        if index == 0:
            return self.prepend_items(value)
        if index == self.length:
            return self.append_items(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index not in range(self.length):
            return "Unbound Node"
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop_items()
        prev = self.get(index-1)
        # temp, prev.next = prev.next, temp.next
        temp = prev.next
        prev.next = temp.next

        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


linked_list = LinkedList(4)


# Adding elements
linked_list.append_items(1)
linked_list.append_items(2)

print(linked_list.pop_items())
print(linked_list.pop_items())
print(linked_list.pop_items())


linked_list.print_list()


linked_list.append_items(2)
linked_list.append_items(3)
linked_list.append_items(4)
linked_list.append_items(5)
linked_list.append_items(6)
linked_list.append_items(7)
linked_list.append_items(8)
linked_list.append_items(9)

print("after adding elements :  ")

# printing elements

linked_list.print_list()


# pop items in linked list

linked_list.pop_items()
linked_list.pop_items()
linked_list.pop_items()
linked_list.pop_items()
linked_list.pop_items()

print("After removing items ")
linked_list.print_list()


# prepending items in linked list

linked_list.prepend(12)
linked_list.prepend(11)
linked_list.prepend(10)

print("After prepending items ")
linked_list.print_list()


print("getting elements")
getting_elements = linked_list.get(2)
print(getting_elements.value)  # type: ignore
getting_elements = linked_list.get(-1)
print(getting_elements)

print("inserting items")
linked_list.insert(2, 456)
linked_list.print_list()

print("after removing")

linked_list.remove(2)
linked_list.print_list()


print("after reversing")
linked_list.reverse()
linked_list.print_list()
