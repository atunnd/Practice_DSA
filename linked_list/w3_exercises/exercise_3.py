'''
Write a Python program to search a specific item in a singly linked list and return true if the item is found 
otherwise return false.
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
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
    
    def print_linked_list(self):
        iter_node = self.head
        while(iter_node):
            print(f'[{iter_node.data}]')
            iter_node = iter_node.next
    
    def search_node(self, key):
        iter_node = self.head
        while(iter_node):
            if iter_node.data == key:
                return True
            iter_node = iter_node.next
        return False

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 10, 2):
        ll.add_node(i)
    ll.print_linked_list()

    query = 2
    if ll.search_node(query):
        print(f"Found {query} in the list!")
    else:
        print(f"{query} is not in the list")
    
    query2 = 3
    if ll.search_node(query2):
        print(f"Found {query2} in the list!")
    else:
        print(f"{query2} is not in the list")