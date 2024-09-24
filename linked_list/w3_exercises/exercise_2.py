'''
Write a Python program to find the size of a singly linked list.
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f"Data: {self.data} - Next: {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_linked_lest(self):
        iter_node = self.head
        while(iter_node != None):
            print(iter_node.data)
            iter_node = iter_node.next

    def get_length(self):
        ll_length = 0
        iter_node = self.head
        while(iter_node != None):
            ll_length += 1
            iter_node = iter_node.next

        return ll_length

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 10, 2):
        ll.add_node(i)
    ll.print_linked_lest()
    print(f"Length of linked list: {ll.get_length()}")