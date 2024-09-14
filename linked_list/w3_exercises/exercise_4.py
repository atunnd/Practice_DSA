'''
Problem: Write a Python program to access a specific item in a singly linked list using index value.
Solution: Using a counter variable initialized with 0 and loop through the linked list. Increase the counter
          for every node until it reaches the index value. Otherwise, return -1 if the given index value is out
          of the range. 
Test case:
1. Linkedlist: (), Index: 5 => -1 (Pass)
2. Linkedlist: (1) -> (2) -> (3), Index: 3 => -1 (Pass)
3. Linkedlist: (1) -> (2) -> (3), Index: 2 => 2 (Pass)
'''

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
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def find_node_by_index(self, key_index):
        if self.check_empty():
            return -1
        
        idx_count = 0
        iter_node = self.head
        while(iter_node):
            if idx_count == key_index:
                return idx_count
            idx_count+=1
            iter_node = iter_node.next

        return -1
    
    def print_linked_list(self):
        iter_node = self.head
        while(iter_node):
            print(f'[{iter_node.data}]')
            iter_node = iter_node.next

    def check_empty(self):
        if self.head:
            return False
        return True
    
if __name__ == '__main__':
    ll = LinkedList()
    
    # test case 0
    test_0 = ll.find_node_by_index(5)
    print(f"Test case 0: {test_0}")

    for i in range(1, 4):
        ll.add_node(i)
    # test case 1
    test_1 = ll.find_node_by_index(3)
    print(f"Test case 1: {test_1}")

    # test case 2
    test_2 = ll.find_node_by_index(2)
    print(f"Test case 2: {test_2}") 