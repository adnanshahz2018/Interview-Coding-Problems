
string = '[()]{}{[()()]()}'
# string = '[(])'
# string = '{([])}'

def validate_order(string):
    stack = []
    view = {   
        '[': 0,
        ']': 0,
        '{': 0,
        '}': 0,
        '(': 0,
        ')': 0
    }

    for s in string:    view[s] += 1 
        
    if ( (not (view['['] + view[']']) % 2 == 0) or 
    (not (view['{'] + view['}']) % 2 == 0) or 
    (not (view['('] + view[')']) % 2 == 0) ):
        print(False)
    else:
        print(True)

def new_func(string):
    s = string[0]
    if not (s == '[' or s == '{' or s == '('):  return False

    opener = []
    valid = { '[': ']',    '{': '}',  '(': ')' }

    for s in string:
        print(s, end=" - ")
        if s == '[' or s == '{' or s == '(': 
            opener.append(s)
        if not (s == '[' or s == '{' or s == '('):
            if opener and valid[opener[-1]] == s:
                opener.pop()
                # opener.pop()
                print('\n opener' , opener)
            else:
                print('\n', False)
                return
       
    print()
    if opener:
        print('opener', opener)
        print(False)
        return False
    else:
        print('\n', True)

# string = input('string: ')
# validate_order(string)
new_func(string)

# ... 