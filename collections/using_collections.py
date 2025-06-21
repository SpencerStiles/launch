print(range(0, 25, 3)[6])

phrase = 'Launch School'
index = phrase.find('c')
print(phrase[index:index + 6])

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
new_tuple = tuple(my_list[1:4])
print(new_tuple)

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

# The list, set, and dict are mutable, so can't be used

print('abc-def'.isalpha())   # False
print('abc_def'.isalpha())   # False
print('abc def'.isalpha())   # False
print('abc def'.isalpha() and   # False
      'abc def'.isspace())   #
print('abc def'.isalpha() or   # False
      'abc def'.isspace())   #
print('abcdef'.isalpha())   # True
print('31415'.isdigit())   # True
print('-31415'.isdigit())   # False
print('31_415'.isdigit())   # False
print('3.1415'.isdigit())   # False
print(''.isspace())   # False

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
pieces = info.split(':')
fixed_string = '+'.join(pieces)
print(fixed_string)

# Line 3 is giving the index of the sliced string
# Line 4 is giving the index of the whole string, only 
# looking within a certain range

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

print('johnson' in 'Joe Johnson')    # false
print('sen' not in 'Joe Johnson')    # true
print('Joe J' in 'Joe Johnson')    # true
print(5 in range(5))    # false
print(5 in range(6))    # true
print(5 not in range(5, 10))    # false
print(0 in range(10, 0, -1))    # false
print(4 in {6, 5, 4, 3, 2, 1})    # true
print({1, 2, 3} in {1, 2, 3})    # false
print({3, 2} in {1, frozenset({2, 3})})    # true

def is_3_in(list):
    if 3 in list:
        print('True')
    else:
        print('False')

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

is_3_in(numbers1)
is_3_in(numbers2)
is_3_in(numbers3)
is_3_in(numbers4)
is_3_in(numbers5)

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) # True
print('Butter' in cats) # False
print('Butter' in cats[3]) # True
print('cheddar' in cats) # False

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

zipped = zip(my_str, my_list, my_tuple, my_range)
print(list(zipped))

['Cat', 'Bird', 'Snake']