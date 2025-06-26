age = int(input('How old are you?'))
years = 10

print('You are ' + str(age) + ' years old.')
i = 0
while i < 4:
    print('In ' + str(years) + ' years, you will be ' + str(age + years) + ' years old.')
    years += 10
    i += 1

