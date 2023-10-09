class Solution:
    # initializing variables
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def is_permutation(self):
        # Check if the lengths are equal
        if len(self.str1) != len(self.str2):
            return False
        
        # Sort both strings
        sorted_str1 = sorted(self.str1)
        sorted_str2 = sorted(self.str2)
        
        # Compare the sorted strings
        return sorted_str1 == sorted_str2


# Example usage:
str1 = str(input("Enter first string: "))
str2= str(input("Enter second string: "))

result = Solution(str1, str2)

if result.is_permutation():
    print(f'"{str1}" is a permutation of "{str2}".')
else:
    print(f'"{str1}" is not a permutation of "{str2}".')
