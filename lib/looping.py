#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()    

#def square_integers(int_list):
    # code goes here!
    
def square_integers(numbers):
    pass
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    # code goes here!
    pass
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()


