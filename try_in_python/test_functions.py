from .structures import SinglyLinkedList, DoublyLinkedList, Stack


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
