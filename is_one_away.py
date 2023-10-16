# Class for comparing two strings to determine if they are one edit (insert, remove, or replace) away from each other.
# It provides a method to check if two strings meet the "One Away" criteria.
class Solution:
    # Initialize variables
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string
    def is_one_away(self):
        # turning strings into lists
        my_first_list = [str(i) for i in self.first_string]
        my_second_list = [str(j) for j in self.second_string]

        res = []
        res2 = []
        # Check if lists were edited 2 or more times
        for i in my_first_list:
            if i not in my_second_list:
                res.append(i)
        for i in my_second_list:
            if i not in my_first_list:
                res2.append(i)

        if len(my_first_list) - len(my_second_list) > 1 or len(my_second_list) - len(my_first_list) > 1:
            return False
        elif len(res) > 1 or len(res2) > 1:
            return False
        else:
            return True

# Example usage

result = Solution("pale", "pie")
print("pale, pie ->", result.is_one_away()) # False (we should replace 'i' by 'l' and add 'a' in second string, but in the book its true, idk why)
result = Solution("pales", "pale")
print("pales, pale ->",result.is_one_away()) # True (remove 's')
result = Solution("pale", "bale")
print("pale, bale ->",result.is_one_away()) # True (replace 'p' with 'b')
result = Solution("pale", "bake")
print("pale, bake ->",result.is_one_away()) # False (two edits needed)

