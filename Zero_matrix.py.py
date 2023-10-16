# In this class we have  4x3 matrix and if we have 0 in row, every value 
# in row we change to zero and the same we do if there is a 0 in columns
class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.zero_rows = set()
        self.zero_columns = set()

    def zero_if_needed(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.matrix[row][col] == 0:
                    self.zero_rows.add(row)
                    self.zero_columns.add(col)

    def process_matrix(self):
        self.zero_if_needed()
        # Set value 0 for rows
        for row in self.zero_rows:
            for col in range(self.columns):
                self.matrix[row][col] = 0
        # Set value 0 for columns
        for col in self.zero_columns:
            for row in range(self.rows):
                self.matrix[row][col] = 0
    # Display the matrix
    def display_matrix(self):
        for row in self.matrix:
            print(row)

# Example usage
matrix = [
    [1, 2, 3, 0],
    [4, 0, 6, 7],
    [8, 9, 10, 11]
]

zero_matrix = Solution(matrix)
zero_matrix.process_matrix()

print("Zeroed Matrix:")
zero_matrix.display_matrix()