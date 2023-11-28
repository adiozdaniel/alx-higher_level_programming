#!/usr/bin/python3
import random

number = random.randint(-10, 10)
result = "is positive is negative is zero"

if number > 0:
    print("{0} {1}".format(number, result[0:11]))
elif number < 0:
    print("{0} {1}".format(number, result[12:23]))
else:
    print("{0} {1}".format(number, result[24:31]))
