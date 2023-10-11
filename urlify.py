# Class which will make URL link from string by changing eac spaces to "%20"
class Solution:
    # initialize variables
    def __init__(self, str1, str_length):
        self.str1 = str1
        self.str_length = str_length
    
    def urlify(self):
        # replace spaces to %20
        str_list = list(self.str1)
        for i in range(self.str_length -1, -1, -1):
            if str_list[i] == ' ':
                str_list[i+2] = '0'
                str_list[i+1] = '2'
                str_list[i] = '%'
        return ''.join(str_list)
# Example usage
str1 = str(input())
str_length = len(str1)
urlifier = Solution(str1, str_length)
result = urlifier.urlify()
print(result)
