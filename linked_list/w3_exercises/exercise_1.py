'''
Write a Python program to create a singly linked list, append some items and iterate through the list.
'''

class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next
    
    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data
    
    def del_data(self):
        del self._data

    def get_next(self):
        return self._next
    
    def set_next(self, next):
        self._next = next
    
    def del_next(self):
        del self._next

    data = property(get_data, set_data, del_data)
    next = property(get_next, set_next, del_next)

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def get_head(self):
        return self._head
    
    def set_head(self, node):
        self._head = node
    
    def del_head(self):
        del self._head
    
    def get_tail(self):
        return self._head
    
    def set_tail(self, node):
        self._tail = node
    
    def del_tail(self):
        del self._tail

    head = property(get_head, set_head, del_head)
    tail = property(get_tail, set_tail, del_tail)

def init_linked_list(ll):
    ll.head = Node()
    ll.tail = Node()

def create_node(data):
    new_node = Node(data)
    return new_node

def create_linked_list(data):
    ll = LinkedList()
    init_linked_list(ll)
    ll.head.data = data[0]
    moving_head = ll.head
    
    for i, value in enumerate(data):
        if i == 0:
            continue
        new_node = create_node(value)
        moving_head.next = new_node
        moving_head = new_node
        if i == len(data)-1:
            ll.tail = moving_head
    return ll

def print_linked_list(head):
    while(head != None):
        print(f"[{head.data}]")
        head = head.next

if __name__ == '__main__':
    ll = create_linked_list([1, 2, 3, 4])
    print_linked_list(ll.head)

    ll2 = create_linked_list([4, 3, 2, 1])
    print_linked_list(ll2.head)