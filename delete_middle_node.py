# This class represents a singly linked list, and provides a method to delete a specified node from the list.
# The deletion operation is performed by copying data from the next node and updating the next pointer
# allowing for the removal of the specified node without direct access to the preceding node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def delete_middle_node(node_to_delete):
        if node_to_delete is None or node_to_delete.next is None:
            # Can not delete the last node or None node
            return
        
        # Copy data from the next node to the current node
        node_to_delete.data = node_to_delete.next.data

        # Update the next pointer to skip the next nOde
        node_to_delete.next = node_to_delete.next.next
    # function to print the linked list
    def display_linked_list(head):
        current = head

        while current:
            print(current.data, end = '->')
            current = current.next

        print("None")

# Example usage
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print('The node c from the linked list is:')
LinkedList.display_linked_list(a)

# Delete the middle node 'c'
LinkedList.delete_middle_node(c)

print('Nothing is returned, but the new linked list loosk like: ')
LinkedList.display_linked_list(a)

