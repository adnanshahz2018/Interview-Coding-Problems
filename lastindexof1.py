# COMPLETED 

A = [1,0,0,0,0,1,1,0]

def findindex(A):
    index = -1 

    for i in range(len(A)):
        if (A[i] == 1):
            index = i
    return index

print(findindex(A))

# ...

