# In this class we check if second string is a permutation of first string
class PermutationChecker:
    # initializing variabless
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string

    def is_permutation(self):
        # Check if the lengths are equal
        if len(self.first_string) != len(self.second_string):
            return False
        
        # Sort both strings
        sorted_first_string = sorted(self.first_string)
        sorted_second_string = sorted(self.second_string)
        
        # Compare the sorted strings
        return sorted_first_string == sorted_second_string


# Example usage:
# I used inputs, because there are no given strings in the book
first_string = str(input("Enter first string: "))
second_string= str(input("Enter second string: "))

result = PermutationChecker(first_string, second_string)

if result.is_permutation():
    print(f'"{first_string}" is a permutation of "{second_string}".')
else:
    print(f'"{first_string}" is not a permutation of "{second_string}".')

