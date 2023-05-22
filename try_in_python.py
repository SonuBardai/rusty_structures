class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, value):
        self.head = SinglyNode(value, None)

    def print(self):
        pointer = self.head
        print("head", end="")
        while pointer:
            print(" => {pointer.value}", end="")
            pointer = pointer.next
        print("\n")

    def insert(self, value):
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        new_node = SinglyNode(value, None)
        pointer.next = new_node

    def delete(self, value):
        """
        Deletes first instance of `value` in the linked_list
        """
        pointer = self.head
        if pointer.value == value:
            self.head = self.head.next
            return
        while pointer.next:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next


class DoublyNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, value):
        self.head = DoublyNode(value)
        self.tail = self.head

    def insert_at_head(self, value):
        new_head_node = DoublyNode(value=value, prev=None, next=self.head)
        self.head.prev = new_head_node
        self.head = new_head_node

    def insert_at_tail(self, value):
        new_tail_node = DoublyNode(value=value, prev=self.tail, next=None)
        self.tail.next = new_tail_node
        self.tail = new_tail_node

    def delete_at_head(self):
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_tail(self):
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_value_from_head(self, value):
        pointer = self.head
        while pointer:
            if pointer.value == value:
                if pointer.prev:
                    pointer.prev.next = pointer.next
                if pointer.next:
                    pointer.next.prev = pointer.prev
                break
            pointer = pointer.next

    def delete_value_from_tail(self, value):
        pointer = self.tail
        while pointer:
            if pointer.value == value:
                if pointer.next:
                    pointer.next.prev = pointer.prev
                if pointer.prev:
                    pointer.prev.next = pointer.next
                break
            pointer = pointer.prev

    def print_forwards(self):
        pointer = self.head
        print(f"head", end="")
        while pointer:
            print(f" <=> {pointer.value}", end="")
            pointer = pointer.next
        print(" <=> tail")

    def print_backwards(self):
        pointer = self.tail
        print("tail", end="")
        while pointer:
            print(f" <=> {pointer.value}", end="")
            pointer = pointer.prev
        print(" <=> head")


def test_singly_linked_list():
    linked_list = SinglyLinkedList(123)
    linked_list.print()
    linked_list.insert(456)
    linked_list.insert(789)
    linked_list.insert(980)
    linked_list.insert(352)
    linked_list.print()
    linked_list.delete(980)
    linked_list.print()


def test_doubly_linked_list():
    linked_list = DoublyLinkedList(123)
    linked_list.print_forwards()
    linked_list.insert_at_head(456)
    linked_list.insert_at_head(1010)
    linked_list.print_forwards()
    linked_list.insert_at_tail(789)
    linked_list.insert_at_tail(1210)
    linked_list.insert_at_tail(1698)
    linked_list.print_forwards()
    linked_list.delete_at_head()
    linked_list.print_forwards()
    linked_list.delete_at_tail()
    linked_list.print_forwards()
    linked_list.delete_value_from_head(123)
    linked_list.print_forwards()
    linked_list.delete_value_from_tail(789)
    linked_list.print_forwards()


class Stack(DoublyLinkedList):
    def __init__(self, value):
        self.head = self.tail = self.top = DoublyNode(value)

    def push(self, value):
        self.insert_at_tail(value)

    def pop(self):
        self.delete_at_tail()

    def print(self):
        pointer = self.tail
        print("Top")
        while pointer:
            print(pointer.value)
            pointer = pointer.prev
        print("-" * 3)
        print("\n")


def test_stack():
    stack = Stack(1)
    stack.push(2)
    stack.print()
    stack.pop()
    stack.print()
    stack.push(3)
    stack.push(4)
    stack.print()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()


if __name__ == "__main__":
    # test_singly_linked_list()
    # test_doubly_linked_list()
    test_stack()
