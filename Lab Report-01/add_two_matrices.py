# Simple matrix addition
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

print(result)