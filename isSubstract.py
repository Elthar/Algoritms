# In this claboth_strings we check if second_string is a substraction of first_string
class Solution:
    def __init__(self, first_string):
        self.first_string = first_string

    def is_substring(self, first_string, second_string):
        # Placeholder function for checking if second_string is a substring of first_string
        # We can replace this with our own implementation or use Python's 'in' operator
        return second_string in first_string

    def is_rotation(self, second_string):
        if len(self.first_string) == len(second_string) and len(self.first_string) > 0:
            # Concatenate self.first_string with itself to create a string containing all rotations
            both_strings = self.first_string + self.first_string

            # Check if second_string is a substring of both_strings
            return self.is_substring(both_strings, second_string)

        return False

# Example usage

first_string =  "waterbottle"
second_string = "erbottlewat"

rotator = Solution(first_string)
result = rotator.is_rotation(second_string)
# Output should be True if second_string is substraction of first_string, otherwise it returns False
print(result)  
