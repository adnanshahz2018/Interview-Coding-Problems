
string = '123006'

def atoi(string):
    integers = ['0' , '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number = 0

    for i in range(len(string)-1, -1, -1):
        print(i)
        if string[i] not in integers:
            print('Non-integer {} found at place {}'.format(string[i], i))
            return
        num = convert(string[i])
        base = findbase(len(string)-i-1)
        number += num*base
    
    print('number = ', number)
    print('number + 2 = ', number + 2)


def convert(value):
    return int(value)

def findbase(value):
    num = 1
    print('value = ', value)
    for i in range(value):
        num *= 10
    return num

atoi(string)