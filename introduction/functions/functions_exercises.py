# 1 - We get an error for an out of scope variable, since print is
# in the global scope and doesn't have access to the variable inside the
# function. 

# 2 - This should print 'qux', since the variable was reassigned inside the
# function, but lives in the global scope. - I was wrong, it's bar, this must
# be a difference from what I'm used to in Javascript.

foo = 'bar'
def set_foo():
    foo = 'qux'
set_foo()
print(foo)

def multiply(number1, number2):
    return f'{number1} * {number2} = {number1 * number2}'

number1 = float(input("What is the first number to be multiplied? "))
number2 = float(input("What is the second number? "))
print(multiply(number1, number2))



def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# function name - multiply_numbers
# function arguments - 2, 3, 4
# function definition - everything except the call (product = etc)
# function body - result = num1 * num2 * num3; return result
# function parameters - num1, num2, num3
# function invocation - multiply_numbers(2, 3, 4)
# function return value - result (24 in this case)
# all identifiers - multiply_numbers, num1, num2, num3, result, and product

# Nothing, it returns a value but doesn't print anything

# Nothing, the function returns before it prints anything

# I think it will print 'Hello', and then error

# I think it will print 42 and 3.141592, and then error

# I think it will print the 3 arguments passed in by the function call, overriding the default
# values in the function definition

# It will print the two arguments passed in, and then the default value for the third parameter, 2.

# It will print the one argument passed in, and then the two default values for the second and third parameter.

# This will error, as there is no value for the first parameter.

# This will error, as there is no value for the third parameter.

# Multiply, left, right, get_num, prompt, float, input, first_number, second_number, 
# product, product, print.

# multiply - global
# left, right - local
# get_num - global
# prompt - local
# float, input - built-in
# first_number, second_number, product - global
# print - built-in

# multiply - function name, 1, 9
# get_num - function name, 3, 7, 8
# left, right - parameter, 1, 2
# prompt - parameter, 4, 5

# say is a function name. print, input and max are built-in functions. .upper() and .lower() are methods

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

set_1 = any(remainders_3(numbers_1))
set_2 = any(remainders_3(numbers_2))
set_3 = any(remainders_3(numbers_3))
set_4 = any(remainders_3(numbers_4))

print(set_1, set_2, set_3, set_4)

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)), 
      all(remainders_5(numbers_2)),
      all(remainders_5(numbers_3)), 
      all(remainders_5(numbers_4)))
