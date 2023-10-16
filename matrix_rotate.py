# In this class we just rotate the given matrix 
class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def rotate_90_degrees(self):
        # Transpose the matrix
        for i in range(self.n):
            for j in range(i, self.n):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        # Reverse the order of elements in each row
        for i in range(self.n):
            self.matrix[i] = self.matrix[i][::-1]

    def display_matrix(self):
        for row in self.matrix:
            print(row)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotator = Solution(matrix)
rotator.rotate_90_degrees()

print("Rotated Matrix:")
rotator.display_matrix()
