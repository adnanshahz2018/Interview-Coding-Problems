# COMPLETED


# A = [[1,2,3], 
#     [4,5,6], 
#     [7,8,9]]


# A = [   [ 1, 2, 3, 4 ], 
#         [ 5, 6, 7, 8 ], 
#         [ 9, 10, 11, 12 ], 
#         [ 13, 14, 15, 16 ],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24] ]
A = [[1],[2], [3], [4], [5], [106]]


rowend = row = len(A)           # the end boundary for traversal in a row
colend = col = len(A[0])        # the end boundary for traversal in a column

print(row)
print(col)
colstart = rowstart = 0

count = 0

# comments are 4 by 4 matrix
while (count < row*col):
    print('line')
    for i in range(colstart,colend):        #iter-1,  1 2 3 4   #2-iter 6, 7
        print(A[colstart][i], end = " , ")
        count +=1
    
    if (count >= row*col):   break

    rowstart +=1        # 1 ,  2
    colend -= 1         # 0 ,  2        

    for i in range(rowstart,rowend):       #iter-1 8 12 16         #2-iter 11, 15
        print(A[i][colend], end=" ,  ")
        count +=1
    if (count >= row*col):   break

    rowend -=1          # 3

    for i in range(colend-1,colstart-1, -1):    #iter-1 15 , 14, 13
        print(A[rowend][i], end=" , ")
        count +=1
    if (count >= row*col):   break
    
    # rowend -= 1  # 3

    for i in range(rowend-1,rowstart-1, -1):    #iter-1  9, 5
        print(A[i][colstart], end=" , ")
        count +=1
    if (count >= row*col):   break

    colstart +=1       # 1
