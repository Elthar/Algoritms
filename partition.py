# This class represents a singly linked list and provides methods for appending nodes and partitioning the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Append a new node with the given data to the end of the linked list.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def partition(self, x):
        # Partition the linked list around the value x, such that nodes less than x come before nodes greater than or equal to x.
        # If x is contained within the list, it appears anywhere in the "right partition."
        less_head = less_tail = Node(0)
        equal_head = equal_tail = Node(0)
        greater_head = greater_tail = Node(0)

        current = self.head

        while current:
            if current.data < x:
                less_tail.next = current
                less_tail = less_tail.next
            elif current.data == x:
                equal_tail.next = current
                equal_tail = equal_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next

            current = current.next

        less_tail.next = equal_head.next
        equal_tail.next = greater_head.next
        greater_tail.next = None

        self.head = less_head.next

    def display(self):
        # Display the linked list.
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(3)
    my_list.append(5)
    my_list.append(8)
    my_list.append(5)
    my_list.append(10)
    my_list.append(2)
    my_list.append(1)

    print("Original Linked List:")
    my_list.display()

    partition_value = 5
    my_list.partition(partition_value)

    print(f"Linked List after partitioning around {partition_value}:")
    my_list.display()