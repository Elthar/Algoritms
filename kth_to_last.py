# This algorithm finds the kth to last element of a singly linked list.
# It does this by using two pointers 'slow' and 'fast' and the 'fast' pointer is moved k nodes ahead of 'slow'.
# Then both pointers are moved together until 'fast' reaches the end of the list.
# At this point 'slow' will be  kth to last element.
# The algorithm handles cases where k is out of bounds or the list is empty.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node the head
            self.head = new_node
        else:
            # Traverse the list to find the last node and append the new node to it
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_kth_to_last(self, k):
        if k < 1:
            return None

        slow = self.head
        fast = self.head

        # Move the 'fast' pointer k nodes ahead
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        # Move 'slow' and 'fast' pointers together until 'fast' reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Return the data of the 'slow' pointer, which is the kth to last element
        return slow.data

# Example usage

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

k = 5
kth_to_last = my_list.find_kth_to_last(k)
if kth_to_last is not None:
    if k == 1:
        print(f"The {k}st to last element is {kth_to_last}")
    elif k == 2:
        print(f"The {k}nd to last element is {kth_to_last}")
    elif k == 3:
        print(f"The {k}rd to last element is {kth_to_last}")
    else:
        print(f"The {k}th to last element is {kth_to_last}")
    
else:
    print("Invalid input for k.")