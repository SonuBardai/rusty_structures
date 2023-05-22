use std::{ptr::NonNull, rc::Rc};

#[derive(Clone, Copy)]
pub struct Node<T> {
    pub value: T,
    pub next: Option<NonNull<Node<T>>>,
}

impl<T> Node<T> {
    pub fn new(value: T) -> Self {
        Node {
            value: value,
            next: None,
        }
    }
}

pub struct RustLinkedList<T> {
    pub head: Option<Node<T>>,
    length: u32,
}

impl<T> RustLinkedList<T> {
    pub fn new(value: Option<T>) -> Self {
        match value {
            Some(value) => Self {
                head: Some(Node {
                    value: value,
                    next: None,
                }),
                length: 1,
            },
            None => Self {
                head: None,
                length: 0,
            },
        }
    }

    pub fn insert(&mut self, value: Option<T>) {
        match value {
            Some(value) => {
                let mut new_node = Node::new(value);
                new_node.next = NonNull::new(self.head.as_mut().unwrap());
                self.head = Some(new_node);
            }
            None => {
                println!("Cannot insert None");
            }
        }
    }
}
