# Class to check if LinkedList is a palindrome
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
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def is_palindrome(self):
        # Function to reverse a linked list
        def reverse_linked_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Function to compare two linked lists
        def compare_linked_lists(list1, list2):
            while list1 and list2:
                if list1.data != list2.data:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True

        if not self.head:
            return False

        slow = self.head
        fast = self.head

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        reversed_half = reverse_linked_list(slow)

        # Compare the first half with the reversed second half
        return compare_linked_lists(self.head, reversed_half)

# Example usage:

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(2)
my_list.append(1)

result = my_list.is_palindrome()
# Output should be True
print(result)  