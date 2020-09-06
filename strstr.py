
big = 'GeeksForGeeks'
small = 'For'

def strstr(big,small):
    count = 0
    match = ''
    start = 0
    flag = False
    for i in range(len(big)):
        if count != len(small) and big[i] == small[count]:
            start = i
            count += 1
            match += big[i]
        else:
            if match == small: 
                print(start-len(small)+1)
                flag = True
            match = ''
            count = 0
    if not flag:    
        print(-1)


strstr(big, small)