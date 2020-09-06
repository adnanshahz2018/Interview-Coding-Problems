# COMPLETED

A = [25,10,20,15,2,32,90,67,70]

def findpeaks(A):
    peak = []
    if len(A) > 1 and A[0]  >=  A[1]:   peak.append(A[0]) 
    if len(A) > 1 and A[-1] >= A[-2]:   peak.append(A[-1]) 

    for i in range(1,len(A)-1):
        if A[i] > A[i-1] and A[i] >= A[i+1]:
            peak.append(A[i])

    return peak

print(findpeaks(A))

# ... 