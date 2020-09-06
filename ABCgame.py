
import random

class ABCgame:
    shift = 0
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, shift):
        self.shift = shift

    def generate(self):
        num = random.randint(0,25)
        return num, self.abc[num]

    def guess(self, trial):
        actual = self.abc[(index + self.shift) % 26]
        if trial == actual:
            return 1
        return 0

if __name__ == "__main__":
    total = 5
    shift = 2
    abc = ABCgame(shift)

    valid = 0
    for i in range(total):
        index, alpha = abc.generate()
        print(alpha, end='\t')
        valid += abc.guess( input(' '))

    print('\t%%%%  Score = ', str(valid) , '/', str(total), '  %%%%' )