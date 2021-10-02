# Write a generator function that gives you the next number in the Fibonacci sequence.

def map_generator():
    return map(lambda i: i, range(10))


def fibo_generator():
    for i in range(100):
        if i == 0:
            yield i
        elif i == 1:
            yield i

        else:
            yield i


def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

generator = fib()
print(generator.__next__())
print(generator.__next__())
print(next(generator))
