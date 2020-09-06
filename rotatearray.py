
A = [1,2,3,4,5]
A = [2,4,6,8,10,12,14,16,18,20]

def rotatearray(A,D):
    count = D
    B = []
    for i in range(len(A)):
        if D >= len(A): D = 0
        B.append(A[D])
        D += 1
    print(B)

# rotatearray(A,2)
rotatearray(A,3)