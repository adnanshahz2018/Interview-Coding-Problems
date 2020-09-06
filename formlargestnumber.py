''' Uncomplete '''


A = [3,30,34,5,9]

def largestnumber(A):
    num = ''
    values = {}
    for i in range(len(A)):
        peak = checkpeak(A[i])
        values[peak] = A[i]

    for i in range(len(A)+1,-1,-1):
        try:
            s = str(values[i]) 
        except:
            s = ''
        num += s

    print('num = ', num)
    return values

def checkpeak(num):
    num2 = int(num/10)
    # print(num2)
    if num2 == 0:
        return num 
    num2 = checkpeak(num2)

    return num2

def larger(A): 
    num = ''

    for i in range(len(A)):
        print(i,A)
        peak = checkpeak(A[i])
        for j in range(i,len(A)):
            if checkpeak(A[j]) >= peak:
                peak = checkpeak(A[j])
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

    for i in range(len(A)): 
        num += str(A[i])
    
    return num


print(larger(A))

# ...