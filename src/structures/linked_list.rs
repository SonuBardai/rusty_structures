use std::fmt::Debug;

#[derive(Debug)]
pub struct Node<T> {
    value: T,
    next: Option<Box<Node<T>>>, // https://doc.rust-lang.org/rust-by-example/std/box.html
}

impl<T> Node<T> {
    pub fn new(value: T) -> Self {
        return Node { value, next: None };
    }
}

#[derive(Debug)]
pub struct LinkedList<T> {
    head: Node<T>,
    length: u32,
}

impl<T: Debug + PartialEq> LinkedList<T> {
    pub fn new(value: T) -> Self {
        let head = Node::new(value);
        return LinkedList { head, length: 1 };
    }

    pub fn print(&self) {
        let mut pointer = &self.head;
        print!("head => {:?}", pointer.value);
        while pointer.next.is_some() {
            pointer = pointer.next.as_ref().unwrap();
            print!(" => {:?}", pointer.value);
        }
        println!("")
    }

    pub fn insert(&mut self, value: T) {
        let new_node = Node::new(value);
        let mut pointer = &mut self.head;
        while pointer.next.is_some() {
            pointer = pointer.next.as_mut().unwrap();
        }
        pointer.next = Some(Box::new(new_node));
        self.length += 1;
    }
}
