''' Uncomplete '''

A = [16,17,4,3,5,2]
A = [1,2,3,4,0]
A = [7,4,5,7,3]


def findleaders(A):
    leader = []
    leader.append(A[0])
    add_leader = True
    for i in range(1,len(A)):
        j = 0
        while(j < len(leader)):
            if leader[j] < A[i]:
                leader.append(A[i])
                leader.remove(leader[j])
                add_leader = False
                j -= 1 
            else: 
                add_leader = True
            j += 1

        if(add_leader): 
            leader.append(A[i])
    
    return leader


print(findleaders(A))

