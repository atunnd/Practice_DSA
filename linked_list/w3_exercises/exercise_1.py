'''
Write a Python program to create a singly linked list, append some items and iterate through the list.
'''


class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def __str__(self):
        return f"Data: {self._data} - Next: {self._next}"

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

    ''' # Get bug for this block of code? Still dont know why, but i guess it's related to the property
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
    '''
    def create_linked_list_from_array(self, data):
        for i, value in enumerate(data):
            new_node = Node(value)
            if i == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
    
    def add_node(self, data):
        new_node = Node(data)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def print_linked_list(self):
        temp = self._head
        while (temp != None):
            print(f"[{temp.data}]")
            temp = temp.next
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.create_linked_list_from_array([1,5,2,3,45])
    ll.add_node(90)
    ll.print_linked_list()
