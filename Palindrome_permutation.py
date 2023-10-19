from collections import Counter

# This class provides a solution for checking if a given string can be rearranged to form a palindrome
class PermutationChecker:
    def __init__(self, input_string):
        # input_string: The input string to check for a permutation of a palindrome
        self.input_string = input_string

    # Check if the input string is a permutation of a palindrome
    def is_permutation_of_palindrome(self):

        # Remove spaces and convert the string to lowercase
        self.input_string = self.input_string.replace(" ", "").lower()
        
        # Use Counter to count character occurrences
        char_count = Counter(self.input_string)

        odd_count = 0

        # Check if the count of characters with odd frequency is less than or equal to 1
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1

        return odd_count <= 1

# Example usage
# return: True if the string can be rearranged to form a palindrome, False otherwise
input_string = str(input())
result = PermutationChecker(input_string)
print(result.is_permutation_of_palindrome())



