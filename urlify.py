# Class which will make URL link from string by changing eac spaces to "%20"
class Urlifier:
    # initialize variables
    def __init__(self, my_string, str_length):
        self.my_string = my_string
        self.str_length = str_length
    
    def urlify(self):
        # replace spaces to %20
        str_list = list(self.my_string)
        for i in range(self.str_length -1, -1, -1):
            if str_list[i] == ' ':
                str_list[i] = '%20'
        return ''.join(str_list)
# Example usage
my_string = 'Mr 3ohn Smith'
str_length = len(my_string)
urlifier = Urlifier(my_string, str_length)
result = urlifier.urlify()
print(result)

