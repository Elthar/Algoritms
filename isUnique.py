# In this class we check if we have the same values in given list
# False - if it's unique list which doesn't have any repeating values
# True - if this list has only unique values

class Solution:
    def __init__(self, input_string):
        self.input_string = input_string

    def is_unique(self):
        # Create an empty set to store unique characters
        unique_set = set()
        
        # Iterate through each character in the input string
        for char in self.input_string:
            if char in unique_set:
                # If the character is already in the set, it's not unique
                return False
            # Otherwise, add it to the set
            unique_set.add(char)
        
        # If the loop completes without finding duplicate characters, it's unique
        return True

# Example usage
input_string = input("Enter a string: ")

unique_checker = Solution(input_string)
unique = unique_checker.is_unique()

if unique:
    print(f'"{input_string}" is unique')
else:
    print(f'"{input_string}" is not unique')
