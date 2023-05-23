from .doubly_linked_list import DoublyNode, DoublyLinkedList


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
