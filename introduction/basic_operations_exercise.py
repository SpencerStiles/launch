first = 'Spencer'
last = 'Stiles'
full = first + ' ' + last
print(full)

number = 4936
digits = {}
place = len(str(number))
while place > 0:
    place -= 1
    digits[place] = number % 10
    number //= 10
print(digits)

print('5' + '10') # Will print '510' because it is concatenating strings

print(int('5') + int('10'))

foo = ['a', 'b', 'c']
print(foo[3]) # Will result in an error, index range goes from 0-2.

print('foo' == 'Foo') # Will be False, the capital F is a different character

print(int('3.1415')) # Will throw an error because it is not an integer

print('12' < '9') # Will be true because it goes lexicographically, and 1 is less than 9
