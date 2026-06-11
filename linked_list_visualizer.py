import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def insert_after(self, prev_node_data, new_data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node_data} not found.")

    def delete_node(self, key):
        current = self.head
        prev = None

        # If head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None  # Free old head
            return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            print(f"Node with data {key} not found.")
            return

        # Unlink the node from linked list
        prev.next = current.next
        current = None # Free memory

def visualize_operations():
    ll = LinkedList()

    print("--- Initializing Linked List ---")
    ll.append(10) # Appending 10
    ll.append(20) # Appending 20
    ll.append(30) # Appending 30
    ll.display() # Visualizing the current state

    print("\n--- Inserting 15 after 10 ---")
    ll.insert_after(10, 15) # Inserting 15 after 10
    ll.display() # Visualizing the state after insertion

    print("\n--- Deleting node with data 20 ---")
    ll.delete_node(20) # Deleting node with data 20
    ll.display() # Visualizing the state after deletion

    print("\n--- Deleting head node (10) ---")
    ll.delete_node(10) # Deleting the head node
    ll.display() # Visualizing the state after deleting head

    print("\n--- Attempting to delete non-existent node (50) ---")
    ll.delete_node(50) # Attempting to delete a non-existent node
    ll.display() # State remains unchanged

if __name__ == "__main__":
    visualize_operations()
