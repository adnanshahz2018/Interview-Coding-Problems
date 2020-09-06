#   COMPLETED

A = [4,3,7,8,6,2,1]
A = list(range(12,20))
A = [11,12,23,24,25,10]
# A = [1,4,3,2]

def zigzag(A):
    Z = []
    A.sort()
    print('sorted = ',A)
    if (len(A)%2 == 0): 
        jump = int(len(A)/2)
        print('jump = ', jump)
        for i in range(int(len(A)/2)):
            Z.append(A[i])
            Z.append(A[i + jump])
    else: 
        jump = int(len(A)/2)
        print('jump = ', jump)
        for i in range(int(len(A)/2)):
            Z.append(A[i])
            if A[i + jump] != A[-2]:
                Z.append(A[i + jump])
        Z.append(A[-1])
        Z.append(A[-2])
    
    return Z

print('zigzag = ', zigzag(A))    


# ...