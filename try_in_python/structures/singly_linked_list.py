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
        if self.head.value == value:
            self.head = self.head.next
            return
        while pointer.next:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
