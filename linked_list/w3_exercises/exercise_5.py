'''
Problem: Write a Python program to set a new value of an item in a singly linked list using index value.
My solution: Check for the list is empty or not. If its not empty, using a counter variable to loop through the list
            until it reaches the index value and set the new value for that index. If the task is done successfully, return 1.
            Return -1 if not found index or the list is empty
Test case:
1. Linkedlist: ..., Index value = -1, New data = 5 => -1 
2. Linkedlist: (1), Index value = 1, New data = 3 => -1
3. Linkedlist: (1) -> (2) -> (3), Index value = 1, New data = 5 => 1
4. Linkedlist: (1) -> (2) -> (3) -> (4), Index value = 3, New data = 10 => 1
'''
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"Data: {self.data}, Next address: {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        new_node =  Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def check_empty(self):
        if self.head:
            return False
        return True
    
    def print_linked_list(self):
        if self.check_empty():
            return
        iter_node = self.head
        while iter_node:
            sys.stdout.write(f"[{iter_node.data}]")
            iter_node = iter_node.next
        
    def replace_data_with_index(self, key_index, key_data):
        if self.check_empty():
            return -1
        iter_node = self.head
        idx_count = 0
        while iter_node:
            if key_index == idx_count:
                iter_node.data = key_data
                return 1
            iter_node = iter_node.next
            idx_count +=1
        
        return -1

if __name__ == "__main__":
    ll = LinkedList()

    # Test case 0
    test_0 = ll.replace_data_with_index(-1, 5)
    print(f"Test 0: {test_0}")

    ll.add_node(1)

    # Test case 1
    test_1 = ll.replace_data_with_index(1, 3)
    print(f"Test 1: {test_1}")

    ll.add_node(2)
    ll.add_node(3)
    # Test case 2
    test_2 = ll.replace_data_with_index(1, 5)
    print(f"Test 2: {test_2}")

    ll.add_node(4)
    # Test case 3
    test_3 = ll.replace_data_with_index(3, 10)
    print(f"Test 3: {test_3}")