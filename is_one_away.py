class Solution:
    # Initialize variables
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def is_one_away(self):
        # turning strings into lists
        list1 = [str(i) for i in self.str1]
        list2 = [str(j) for j in self.str2]

        res = []
        res2 = []
        # Check if difference between two lists is 2 or more
        for x in list1:
            if x not in list2:
                res.append(x)
        for x in list2:
            if x not in list1:
                res2.append(x)

        if len(res) > 1 or len(res2) > 1:
            return False
        else:
            return True

# Input 2 strings and check if it was edited once or more times
# True - if we can get strx1 by editing strx2 only with one move, False - if we have to edit strx1 two or more times to get strx2
str1 = str(input())
str2 = str(input())

result = Solution(str1, str2)
final_result = result.is_one_away()
print(final_result)