# In this class we remove duplicates from given list
class Solution:
    def __init__(self, my_list):
        self.my_list = my_list
    
    def remove_dups(self):
        # function set() in python can automatically remove duplicates from list
        # but it returns dictionary by default, so we change it to list 
        new_list = list(set(self.my_list))
        return new_list

# Example usage

result = Solution([1,1,2,3,3,4,5,4])
final_result = result.remove_dups()
print(final_result)
    
