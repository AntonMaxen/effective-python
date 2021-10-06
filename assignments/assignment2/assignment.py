import time
import sys
# Write a generator function that gives you the next number in the Fibonacci sequence. 
def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

# Write a function that takes in a list of strings and returns every character in those strings
listring = lambda strings: [list(string) for string in strings]


# Write a function (that uses reduce) that converts following dict.
red = lambda d: reduce(lambda a, b: [*a, {**b[1], 'name': b[0]}], d.items(), [])


# Write a decorated called lowercased that can be used to turn any result of a function
# returning a string into lowercase
def lowercased(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return wrapper


# Write a decorator called tired that makes a function sleep before returning its result.
def tired(s):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Sleeping for: {s} seconds')
            sys.stdout.flush() # Dont buffer previous output.
            time.sleep(s)
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


# Use a lambda and the built-in function function filter to filter out all numbers greater than num.
greater_then = lambda arr, num: filter(lambda x: x > num, arr) 
