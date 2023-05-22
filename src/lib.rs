use structures::linked_list::RustLinkedList;

mod structures;

pub fn run() {
    let mut linked_list: RustLinkedList<u8> =
        structures::linked_list::RustLinkedList::new(Some(123));

    linked_list.insert(Some(19));

    // print the linked list
    match linked_list.head {
        Some(head_node) => {
            print!("head => {}", head_node.value);
            // while head_node.next.is_some() {
            let head_pointer = head_node.next.unwrap();
            unsafe {
                let head_node = *(head_pointer.as_ref());
                print!(" => {}", head_node.value)
            }
            // }
        }
        None => {
            print!("Empty node");
        }
    }
}
