
string = '1.like.this.program.very.much'


def reverse_words(string):
    reverse = ''
    parts = string.split('.')
    print(parts)
    for i in range(len(parts)-1,-1,-1):
        reverse += parts[i]
        if not i == 0:   reverse += '.'

    print(reverse)


reverse_words(string)

    