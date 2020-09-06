#   COMPLETED

A = [4,2,5,7]
# A = [4,3,2,7,8,9]
A = [11,9,12]

def check(A):
    flag = False
    for i in range(1,len(A)-1):
        flag = check2(i,A)
        if flag: 
            return i, A[i]
    return -1, -1

def check2(index,A):
    flag = False
    for i in range(index):
        if A[i] <= A[index]:
            flag = True
        else:
            print('false = ', index)
            return False
    for i in range(index+1,len(A)):
        if A[i] >= A[index]:
            flag = True
        else:
            print('false = ', index)
            return False

    print('true = ', index)
    return flag


print(check(A))
# ...