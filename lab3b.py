#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 120669221

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    sum = number1 + number2
    return sum

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    substraction = number1 - number2
    return substraction

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    multiplication = number1 * number2
    return multiplication

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
