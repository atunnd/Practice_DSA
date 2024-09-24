'''
Problem: Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward, backward).
My solution: Just like the single linked list. Now, we add a previous address to the node.
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Data: {self.data}, Next address: {self.next}, Previous address: {self.prev}"

class double_linked_list():
    def __init__(self):
        self.header = None
        self.tail = None
    
    def add_node(self, data):
        new_node = node(data)
        if self.header == None:
            self.header = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def check_empty(self):
        if self.header == None:
            print("The double linked list is empty!")
            return True
        return False

    def print_forward(self):
        if self.check_empty():
            return
        iter_node = self.header
        while iter_node:
            print(f"[{iter_node.data}]")
            iter_node = iter_node.next
    
    def print_backward(self):
        if self.check_empty():
            return
        iter_node = self.tail
        while iter_node:
            print(f"[{iter_node.data}]")
            iter_node = iter_node.prev


if __name__ == "__main__":
    dll1 = double_linked_list()
    for i in range(10):
        dll1.add_node(i)
    print("Print forward:")
    dll1.print_forward()
    print("Print backward:")
    dll1.print_backward()