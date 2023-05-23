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
