# COMPLETED
 
# A type of activity selection problem
# Assuming A and Sorted in Ascending Order

A = [900,  940, 1100, 1500]
Z = [910, 1200, 1130, 1900]

A = [900,  1100,  1235]
Z = [1000, 1200, 1240]

# A = [900,  940,  950, 1100, 1500, 1800]
# Z = [910, 1200, 1120, 1130, 1900, 2000]

def countplatfroms(A,Z):
    count = 1
    list_platforms = []
    new_platform = []
    new_platform.append(Z[0])
    list_platforms.append(new_platform)

    for i in range(1,len(A)-1):
        count, list_platforms = check(count, i, A, list_platforms)

    return count

def check(count, i, A, list_platforms):
    for p in list_platforms:
            for j in range(len(p)):
                if p[j] < A[i]:
                    p.remove(p[j])
                    p.append(Z[i])
                    return count, list_platforms
    new_platform = []
    new_platform.append(Z[i])
    list_platforms.append(new_platform)
    return count + 1, list_platforms


print(countplatfroms(A,Z))

#....