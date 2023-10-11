# In this problem we check if it's possible to obtain a mirrored string by simply rearranging the letters. "
# If so, return - True, if not, return - False
class Solution:
    def __init__(self, str1):
        self.str1 = str1

    def is_permutation_of_palindrome(self):
        # remove spaces and convert strings to lowercase
        self.str1 = self.str1.replace(" ", "").lower()
        char_count = {}

        # Check if the character is an alphabet letter.
        for i in self.str1:
            if i.isalpha():
                if i in char_count:
                    char_count[i] += 1
                else:
                    char_count[i] = 1

        odd_count = 0
        
        # Check if the count is odd.
        for j in char_count.values():
            if j % 2 != 0:
                odd_count += 1

        return odd_count <= 1

# Example usage
str1 = str(input('Enter string: '))
result = Solution(str1)
print(result.is_permutation_of_palindrome())


