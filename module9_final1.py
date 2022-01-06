## 7

def my_average(*args):
    total = 0
    for x in args:
        total = total + x
    return total / len(args)

ans7a = my_average(78, 82, 91, 66)
ans7b = my_average(56, 89, 76, 100)

print('#7: ', ans7a, ans7b)

## 8

def print_last_info(**kwargs):
    for key, value in kwargs.items():
        string = ("{} is {}".format(key,value))
    return string

ans8a = print_last_info(Name= "Rosie", Age= 33, Profession= "Data Scientist")
ans8b = print_last_info(Name= "Kyle", Age= 28, Profession= "Data Engineer", Phone_Number=4659874982)

print('#8: ', ans8a, ans8b)

## 9

movie = {'Title': 'Inception',
        'Director': 'Nolan',
        'Year': 2010
        }

def print_movie(**kwargs):
    for k, v in kwargs.items():
        string = f'{k}: {v}'
        return string
        
ans9a = print_movie(**movie)
ans9b = print_movie(Music='Zimmer', **movie)

print('#9: ', ans9a, ans9b)






## 10

from typing import AnyStr


def plus_one(x):
    def add_one(x):
        x += 1
        return x
    return add_one(x)

ans10 = plus_one(7)
print('#10: ' + str(ans10))

## 11

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hello():
    return 'hello there'

ans11 = say_hello
#print('#11: ' + ans11)

## 12

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

ans12_ = cities("Paris", "New York")

#print('#12: ' + ans12)

## 13

def function_with_arguments(x, y, z):
    return (x, y, z)

def decorator_passing_arbitrary_arguments(func):
    def wrapper_accepting_arguments(*args):
        print('The positional arguments are', args)
    return wrapper_accepting_arguments

ans13 = decorator_passing_arbitrary_arguments(function_with_arguments(1, 2, 3))