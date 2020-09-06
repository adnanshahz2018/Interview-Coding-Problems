
matrix =    [[1,2,3],
            [4,5,6],
            [7,8,9]]

def rotate_anticlock(matrix):
    rotated = [row[:] for row in matrix]
    print()
    for i in range(len(matrix)-1,-1,-1): # giving number of rows
        for j in range(len(matrix[0])): #giving number of columns
            rotated[len(matrix)-i-1][j] = matrix[j][i] 
    
    for row in rotated:
        print(row)
    return rotated

matrix = rotate_anticlock(matrix)
matrix = rotate_anticlock(matrix)
matrix = rotate_anticlock(matrix)
matrix = rotate_anticlock(matrix)

# print(matrix)
