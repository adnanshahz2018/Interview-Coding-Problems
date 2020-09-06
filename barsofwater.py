''' Uncomplete '''

A = [4,3,0,2,0,0]
# A = [7,4,0,9]
# A = [9,6,9,6,9]

def simplebarsofwater(A):
    firstmax = -1
    for i in range(len(A)): # find  First Max
        if A[i] > firstmax: 
            firstmax = A[i]
    secondmax = -1
    for i in range(len(A)): # find Second Max
        if A[i] > secondmax and A[i] < firstmax:
            secondmax = A[i] 
    
    totalbars = 0
    for i in range(len(A)): # find Max
        if A[i] < secondmax:
            totalbars += secondmax - A[i]

    return totalbars

A = [1,2,0,6,0,5]

def complexbarsofwater(A):
    bars = 0 
    count = 0   
    while count < len(A):
        first = A[count]    # 1: 2
        index, second = check(count,A)
        if index == -1:     
            return bars
        if second != -1:    
            bars += addbars(count, index, A) # 2,4,A:
        count = index

    return bars

def addbars(count, index, A):
    print(count, ',', index, ' = ',  A[count], '-', A[index])
    bars = 0
    if A[count] > A[index]:
        for i in range(count+1, index):
            bars += A[index] - A[i]
    if A[index] >= A[count]:
        for i in range(count+1, index):
            bars += A[count] - A[i]
    print('bars = ', bars)
    return bars

def check(i,A):                 # 0: 
    for j in range(i+1,len(A)):
        if A[j] >= A[i]:
            if j == i+1:
                return j, -1    # j=1, -1
            else:        
                second = A[j]
                # print(i, j)
                return j, A[j]

    return -1, -1


# print(simplebarsofwater(A)) 
print(complexbarsofwater(A))       

#....