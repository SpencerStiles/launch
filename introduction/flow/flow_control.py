False or (True and False) # False
True or (1 + 2) # True
(1 + 2) or True # 3 
True and (1 + 2) # 3
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129 # False
False != (not True) # False
True == 4 # False
False == (847 == '847') # True

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

# Product 2 and Product not found, because the second call uses an integer
# and not a string.

def baz():
    if foo():
        return 'bar'
    else:
        return qux()

# Empty, because the empty list is falsy

def all_caps(word):
    if len(word) > 10:
        return word.upper()
    else:
        return word

def range_finder(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <=100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')