# 1. Upper case the second key alphabetically, in this case CHRIS

import math
print(math.sqrt(37))

from math import sqrt
print(sqrt(37))

import math as m
print(m.sqrt(37))

def sum_of_squares(num1, num2):
    def square(number):
        return number * number

    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

counter = 0
def increment_counter():
    global counter
    counter += 1

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()