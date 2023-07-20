#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("{0} is positive".format(number))
elif number == 0:
    ("{1} is zero".format(number))
else:
    ("{2} is negative".format(number))
