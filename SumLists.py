# In this class we reverse LinkedLists and find the sum of them
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

def add_linked_lists_reverse(list1, list2):
    # Initialize a dummy head node to simplify the code
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Traverse both linked lists
    while list1 or list2 or carry:
        x = list1.val if list1 else 0
        y = list2.val if list2 else 0

        # Calculate the sum and carry
        _sum = x + y + carry
        carry = _sum // 10

        # Create a new node with the calculated value
        current.next = ListNode(_sum % 10)
        current = current.next

        # Move to the next nodes in both linked lists
        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    return dummy_head.next

def reverse_linked_list(head):
    # Reverse a linked list in-place
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_linked_lists_forward(list1, list2):
    # Reverse both linked lists
    reversed_list1 = reverse_linked_list(list1)
    reversed_list2 = reverse_linked_list(list2)
    
    # Add the reversed linked lists using the reverse order function
    result = add_linked_lists_reverse(reversed_list1, reversed_list2)
    
    # Reverse the result back to the forward order
    return reverse_linked_list(result)

# Example usage:
if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()

    # Add elements to list1 and list2 in reverse order (from tail to head)
    list1.append(7)
    list1.append(1)
    list1.append(6)

    list2.append(5)
    list2.append(9)
    list2.append(2)

    print("Input:")
    list1.display()
    print("+")
    list2.display()

    result_reverse = add_linked_lists_reverse(list1.head, list2.head)
    print("\nOutput (Reverse Order):")
    while result_reverse:
        print(result_reverse.val, end=" -> " if result_reverse.next else "\n")
        result_reverse = result_reverse.next

    result_forward = add_linked_lists_forward(list1.head, list2.head)
    print("\nOutput (Forward Order):")
    while result_forward:
        print(result_forward.val, end=" -> " if result_forward.next else "\n")
        result_forward = result_forward.next