# index - idiomatic
# CatName - non-idiomatic - CamelCase instead of snake_case
# lazy_dog - idomatic
# quick_Fox - non-idiomatic - Capitalized letter
# 1stCharacter - illegal - Starts with a number
# operand2 - idiomatic
# BIG_NUMBER - non-idiomatic - SCREAMING_SNAKE_CASE
# pi - non-idiomatic - Symbol

# Class names and constants follow different rules, but not functions.
# Same as above.

# BIG_NUMBER and LAZY_FOX3 are the only idiomatic options. The rest do not use
# SCREAMING_SNAKE_CASE. 1ST starts with a number and the russian character
# is not ASCII.

# Similarly, CatName and BigNumber3 are the only idiomatic Class names. 1st
# is still illegal for starting with a number, everything else uses the wrong
# case or is a non-ASCII character.

name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# 7. The program will change the value of the variable even though it is
# supposed to be a constant, because python doesn't actually support constants.
# They are just for the programmer to observe.

i = 0
balance = 1000
while i < 5:
    balance *= 1.05
    i += 1
print(balance)

# 9. I think my solution for 8 already handled this too.

# obj = 'ABcd' - Reassigns
# obj.upper() - Neither
# obj = obj.lower() - Reassigns
# print(len(obj)) - Neither
# obj = list(obj) - Reassigns
# obj.pop() - Mutates
# obj[2] = 'X' - Mutates
# obj.sort() - Mutates
# set(obj) - Neither 
# obj = tuple(obj) - Reassigns