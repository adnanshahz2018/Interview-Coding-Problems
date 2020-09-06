# COMPLETED

a = [1,2,3,4,5]
b = [2,4,6,7]


def numberofpairs(a,b):
    pairs = []
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if ( a[i]**b[j] > b[j]**a[i]):
                count += 1
                pairs.append( str(a[i]) + ',' + str(b[j]) )
    
    return count, pairs

print (numberofpairs(a,b))




# ...