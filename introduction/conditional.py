value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # we don't care about 9
else:
    print('value is something else')


print(1 or 2 and 3)
print(0 or 2 and 3)
print(1 or 0 and 3)
print(1 or 2 and 0)
print(0 or 0 and 3)
print(0 or 2 and 0)
print(1 or 0 and 0)
print(0 or 0 and 0)

print(1 and 2 or 3)
print(0 and 2 or 3)
print(1 and 0 or 3)
print(1 and 2 or 0)
print(0 and 0 or 3)
print(0 and 2 or 0)
print(1 and 0 or 0)
print(0 and 0 or 0)