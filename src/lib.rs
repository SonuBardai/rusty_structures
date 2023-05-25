use structures::linked_list::LinkedList;
mod structures;

pub fn run() {
    let mut linked_list = LinkedList::new(123);
    linked_list.insert(456);
    linked_list.print();
    linked_list.insert(789);
    linked_list.print();
}
