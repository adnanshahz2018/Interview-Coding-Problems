
A = [1,2,3,6,2,4,9,8]


def sortarray(A):
    merges = []
    mid = len(A)/2
    while mid > 1:
        mid = len(A)/2
        merges.append( A[:int(len(A)/2)] )
        merges.append( A[int(len(A)/2):] )
    print(a1)
    print(a2)

print(sortarray(A))

# ...