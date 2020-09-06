#  COMPLETED

A = [1,3,4,2,5,  9,
    1,1,1,1,1,
    1,1,1,1,1,
    1,1, 1, 2]

def equilibrium(A):
    count = 0
    for i in range(len(A)):
        print('\ni', i)
        leftsum = rightsum = 0
        for j in range(i+1,len(A)):
            # print('j',j)
            rightsum += A[j]
            count += 1
        for k in range(i):
            # print('k',k)
            leftsum += A[k]
            count += 1
        if leftsum == rightsum:
            print('\nCOUNT  =  ', count, '\n')
            return i, A[i]

    print('\nCOunt  =  ', count, '\n')
    return -1, -1

print(equilibrium(A))


#....