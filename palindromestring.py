
string = 'aaaabbaa'
string = 'racecaracecamadamr'

string = 'abcdefghijklmadamabcdefghijklj'

def find_palindrome(string): # the longest pal wil be string / 2 in length
    length = len(string) 
    count = 0
    for z in range(length+1,-1,-1):
        for i in range(len(string)-(z-1)):  # bigger the c => lesser the iterations
            count += 1
            part = string[i:i+z]
            print('part -- ', part)
            if part == part[::-1]:
                print('part = ', part)
                print('length = ', length)
                print('count = ', count)
                return part 


find_palindrome(string)
# ...


