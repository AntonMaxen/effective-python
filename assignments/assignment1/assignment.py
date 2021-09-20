"""Python Assignment 1"""


"""
### Algoriths ###
"""
# 1. Write a Python function to calculate the sum of a list of numbers
my_sum = lambda arr: sum(arr)


# 2. Write a Python function to convert an Integer to a string in any base
get_chars = lambda a, b: [chr(ord(a) + i) for i in range(ord(b) - ord(a) + 1)]
chrs = "".join(get_chars('0', '9') + get_chars('A', 'F'))
to_string = lambda n, b: chrs[n] if n < b else to_string(n // b, b) + chrs[n % b]


# 3. Write a Python function of to recursively calcualte the sum
sum_r = lambda a: sum([sum_r(v) if isinstance(v, list) else v for v in a])


# 5. Write a Python function to solve the Fibonacci sequence using recursion
fibo = lambda n: fibo(n-1) + fibo(n-2) if n > 1 else n


# 6. Write a Python function to get the sum of a non-negative integer.
split_sum = lambda x: sum([int(v) for v in list(str(x))])


# 11. Write a Python function to find the greatest common divisor (gcd) of two integers.
gcd = lambda *a: max([i for i in range(min(a[:2]), 0, -1) if max(a[:2]) % i == 0 and min(a[:2]) % i == 0], default=None)


"""
### Questions ###
"""

# 1. Explain what a variable is.
"""
A variable is a container for a particular datatype.
"""

# 2. Explain what a function is.
"""
A function is a sequence instructions for a specific task. It also go
by the name subprogram, which means that behaves like a program. The function
is often defined with a name so it can get called within the program. If a function
is not named, it is a anonymous function, like lambdas in python.
"""

# 3. Explain what a program is.
"""
A program is usually concised of a larger sequence of instructions for a specific purpose.
Within the program it is normal to use functions(subprograms) or classes to group your data.
"""

# 4. Explain what makes a program effective.
"""
Something that makes a program effective is that it solves a problem effectively, nothing more nothing less.
A effective program doesnt waste resources by doing unnecessary things and doesn't waste time by being to
expensive in time complexity. It is also easy to read the code and the future you or another person wastes 
less time trying to understand the code. The program is also structured in a way which makes it easier to
modify or improve on in the future. Nothing is hardcoded.
"""


# 5. Explain what effective programming is.
"""
Effective programming is a large area of a mindset on how to make your and your future
colleges life easier. Keep it simple, minimize complexity, use design patterns and make your code
reusable. And one really important part is to write tests for your program. Instead of wasting your own valuable time
of trying to test/break your program, write a program that tests your program with a predetermined outcome.
Write your code as if you were writing it for another person to read. Have explaining variable/function names,
write a comment if something gets complex.
"""

# Written by: Anton Maxen
