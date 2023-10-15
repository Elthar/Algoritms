# In this class we check if we have the same values in given list
# False - if it's unique list which doesn't have any repeating values
# True - if this list has only unique values

class Solution:
    #initialize variables
    def __init__(self, input_string):
        self.input_string = input_string

    def is_unique(self):
        # Check if there are same values in list 
        # False - there are at least two same values, True - No same values
        l = len(self.input_string)
        for i in range(l):
            for j in range(i+1, l):
                if self.input_string[i] == self.input_string[j]:
                    return False 
        return True

# Example usage
my_list = []
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))  
c = int(input("Enter third number: "))  
d = int(input("Enter fourth number: "))

my_list.append(a)
my_list.append(b)
my_list.append(c)
my_list.append(d)

unique_checker = Solution(my_list)
unique = unique_checker.is_unique()

if unique:
    print(f"{my_list} is unique")
else:
    print(f"{my_list} is not unique")
