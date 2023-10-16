# In this class we check if str2 is a substraction of str1
class Solution:
    def __init__(self, str1):
        self.str1 = str1

    def is_substring(self, str1, str2):
        # Placeholder function for checking if str2 is a substring of str1
        # We can replace this with our own implementation or use Python's 'in' operator
        return str2 in str1

    def is_rotation(self, str2):
        if len(self.str1) == len(str2) and len(self.str1) > 0:
            # Concatenate self.str1 with itself to create a string containing all rotations
            ss = self.str1 + self.str1

            # Check if str2 is a substring of ss
            return self.is_substring(ss, str2)

        return False

# Example usage

str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))

rotator = Solution(str1)
result = rotator.is_rotation(str2)
# Output should be True if str2 is substraction of str1, otherwise it returns False
print(result)  