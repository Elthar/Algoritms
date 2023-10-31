class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        # Create a new node with the given value
        new_node = ListNode(value)
        
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
        else:
            # Traverse the list to find the last node and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def get_intersection_node(listA, listB):
    def get_length_and_tail(node):
        length = 0
        while node and node.next:
            length += 1
            node = node.next
        return length, node

    # Get the length and tail of both linked lists
    lengthA, tailA = get_length_and_tail(listA.head)
    lengthB, tailB = get_length_and_tail(listB.head)

    # If the tails are not the same, the lists do not intersect
    if tailA is not tailB:
        return None

    currentA, currentB = listA.head, listB.head

    # Adjust the starting positions to have the same remaining length
    if lengthA > lengthB:
        for _ in range(lengthA - lengthB):
            currentA = currentA.next
    elif lengthB > lengthA:
        for _ in range(lengthB - lengthA):
            currentB = currentB.next

    # Traverse both lists until an intersection is found
    while currentA is not currentB:
        currentA = currentA.next
        currentB = currentB.next

    return currentA  # Return the intersection node

# Example usage:
listA = LinkedList()
listA.append('A1')
listA.append('A2')
listA.append('A3')
listA.append('C1')
listA.append('C2')

listB = LinkedList()
listB.append('B1')
listB.append('B2')
listB.head.next.next = listA.head.next.next.next  # Intersect at node C

intersection_node = get_intersection_node(listA, listB)
if intersection_node:
    print(f'Intersection at node {intersection_node.value}')
else:
    print('No intersection found')