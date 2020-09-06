# COMPLETED

A = [0,2,2,2,1,1,0,1,1,1,1,2,2,2,0,0,0,0,2,0,0,0]

def sortarray(A):
    sortedarray = []
    for i in range (3):
        for j in range(len(A)):
            if A[j] == i: sortedarray.append(A[j])
    return sortedarray

def sortstyle_c(A):
    index = 0
    for i in range (3):
        for j in range(len(A)):
            if A[j] == i: 
                temp = A[j]
                A[j] = A[index]
                A[index] = temp 
                index += 1

    return A

print(sortarray(A))
print(sortstyle_c(A))   




