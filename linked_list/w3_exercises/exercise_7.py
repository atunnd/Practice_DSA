'''
Problem: Write a Python program to delete the last item from a singly linked list.
My solution: If the linnked list is empty, return 0. If the length is 1, delete the first node and set both
             header and tail to "None". If the length is more than 1, iterate node from header to the node next to tail.
             Set that the next address of that node to "None" and then, set tail to that node. Return 1 if successfully.
Test case:
1. []. Return 0 (empty list)
2. (1). Return 1 (delete successfully)
3. (1)->(2)->(3). Return 1 (delete successfully)
'''

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"Data: {self.data}, Next address: {self.next}"

class linked_list:
    def __init__(self):
        self.header = None
        self.tail = None
    
    def add_node(self, data):
        new_node = node(data)
        if self.header:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.header = new_node
            self.tail = new_node
    
    def check_empty(self):
        if self.header == None:
            print("The linked list is empty!")
            return True
        return False

    def print_linked_list(self):
        if self.check_empty():
            return
        iter_node = self.header
        while iter_node:
            print(f"[{iter_node.data}]")
            iter_node = iter_node.next
    
    def delete_tail_node(self):
        if self.check_empty():
            return 0
        if self.header == self.tail:
            self.header = None
            self.tail = None
        else:
            iter_node = self.header
            while iter_node:
                if iter_node.next == self.tail:
                    iter_node.next = None
                    self.tail = iter_node
                    break
                iter_node = iter_node.next

        return 1

if __name__ == "__main__":
    ll1 = linked_list()
    
    # First test
    test1 = ll1.delete_tail_node()
    print(f"Test 1: {test1} \n")

    # Second test
    ll1.add_node(1)
    print("Before test 2:")
    ll1.print_linked_list()
    test2 = ll1.delete_tail_node()
    print("After test 2")
    ll1.print_linked_list()
    print(f"Test 2: {test2} \n")

    # Third test
    for i in range(4): 
        ll1.add_node(i)
    print("Before test 3:")
    ll1.print_linked_list()
    test3 = ll1.delete_tail_node()
    print("After test 3:")
    ll1.print_linked_list()
    print(f"Test 3: {test3} \n")