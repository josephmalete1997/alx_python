#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number_new = str(number)
last_digit_string = number_new[len(number_new)-1]
last_digit = int(last_digit_string)
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number,last_digit))
else:
    if number < 0:
        last_digit = 0 - last_digit
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_digit))

