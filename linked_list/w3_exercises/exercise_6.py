'''
Problem: Write a Python program to delete the first item from a singly linked list.
My Solution: First, check the empty list, if empty, return 0. If there is only 1 node, delete that node, set the
             header and tail to NULL. If there are more nodes than 1, set the header to the second node. Return 1 if
             delete successfully.
Test case:
1. []. Return 0 (empty list)
2. (1). Return 1 (delete successfuly)
3. (0)->(1)->(2)->(3)->(4)->(5). Return 1 (delete successfully)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data: {self.data}, Next address: {self.next}"

class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.header:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.header= new_node
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
    
    def delete_first_node(self):
        if self.check_empty():
            return 0
        self.header = self.header.next
        return 1

if __name__ == "__main__":
    ll1 = LinkedList()

    # first test
    test1 = ll1.delete_first_node()
    print(f"Test 1: {test1}\n")

    # second test
    ll1.add_node(1)
    print("Before test 2:")
    ll1.print_linked_list()
    test2 = ll1.delete_first_node()
    print("After test 2:")
    ll1.print_linked_list()
    print(f"Test 2: {test2}\n")

    # third test
    for i in range(6):
        ll1.add_node(i)
    print("Before test 3")
    ll1.print_linked_list()
    test3 = ll1.delete_first_node()
    print("After test 3:")
    ll1.print_linked_list()
    print(f"Test 3: {test3}")


