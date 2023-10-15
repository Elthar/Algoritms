# In this class we remove duplicates from given list
class Solution:
    def __init__(self, my_list):
        self.my_list = my_list
    
    def remove_dups(self):
        # function set() in python can automatically remove duplicates from list
        # but it returns dictionary by default, so we change it to list 
        a = list(set(self.my_list))
        return a

# Example usage
my_list = [1,1,2,3,3,4,5,4]
result = Solution(my_list)
res2 = result.remove_dups()
print(res2)
    
