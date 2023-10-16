# Class for compressing strings
class Solution:
    def __init__(self, string):
        self.string = string

    def compress(self):
        # Compresses the input string using the counts of repeated characters.
        # Returns:
        # The compressed string or the original string if compression is not effective.

        compressed_string = ""
        count = 1

        # Check if the current character is the same as the previous character
        for i in range(1, len(self.string)):

            if self.string[i] == self.string[i - 1]:
                count += 1
            else:
                # If the current character is different, add the previous character and its count to the compressed string
                compressed_string += self.string[i - 1] + str(count)
                count = 1

        compressed_string += self.string[-1] + str(count)
        # Check if the compressed string is shorter than the original string
        if len(compressed_string) >= len(self.string):
            return self.string
        else:
            return compressed_string

# Example usage:

compressor = Solution('aabcccccaaa')
compressed_result = compressor.compress()
print(compressed_result) 
