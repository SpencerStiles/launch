# 1. We never increment the counter variable

age = int(input('How old are you?'))

print('You are ' + str(age) + ' years old.')
years = [10, 20, 30, 40]
for year in years:
    print('In ' + str(year) + ' years, you will be ' + str(age + year) + ' years old.')

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

for number in my_list:
    if number % 2 != 0:
        print(number)

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for number in list:
        if number % 2 == 0:
            print(number)

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

odd_even_list = []
for number in my_list:
    if number % 2 == 0:
        odd_even_list.append('even')
    else:
        odd_even_list.append('odd')

print(odd_even_list)

def find_integers(tuple):
    result = []
    for item in tuple:
        if type(item) == int:
            result.append(item)
    return result


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

dict = { item: len(item) for item in my_set if len(item) % 2 != 0}
print(dict)

def factorial(number):
    index = number -1
    while index:
        number*= index
        index -= 1
    return number

print(factorial(5))

#import random
#
#highest = 10
#while True:
#    number = random.randrange(highest + 1)
#    print(number)
#    if number == highest:
#        break

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    list = my_list[index]
    list_index = 0
    while list_index < len(list):
        number = list[list_index]
        if number % 2 == 0:
            print(number)
        list_index += 1
    index += 1
