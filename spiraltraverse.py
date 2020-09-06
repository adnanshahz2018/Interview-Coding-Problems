# COMPLETED

''' Took 10 minutes to code a lame approach 
    +15 minutes to complete  a generic code
    +10 minutes to complete all the corner cases 
'''



# A = [   [ 1, 2, 3, 4 ], 
#         [ 5, 6, 7, 8 ], 
#         [ 9, 10, 11, 12 ], 
#         [ 13, 14, 15, 16 ],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24] ]

A = [
    [1, 2, 3, 103], 
    [4, 5, 6, 106], 
    [7, 8, 9, 109],
    [27,28,29,112],
    [37,38,39,115],
    [47,48,49,118]
    ]

A = [[1,2,3,4,5,6]]

row = len(A)
col = len(A[0])
rowstart = colstart = 0

total = row*col
count = 0
while(row>0 and col>0):

    for i in range(rowstart, row):  # 1, 4, 7
        print(A[i][rowstart])

    colstart +=1       # 1
    if(row==rowstart or col==colstart): break

    for i in range(colstart, col):
        print(A[row-1][i])

    row -=1     # 2
    if(row==rowstart or col==colstart): break

    for i in range(row-1,rowstart-1, -1):
        print(A[i][col-1])  #col-1 = 2
    
    col -= 1    # 2
    if(row==rowstart or col==colstart): break

    for i in range(col-1, colstart-1, -1):
        print(A[rowstart][i])

    rowstart += 1



# ...