# ==== 1 =====
#  this array contains a hidden message,
#  can you decode it?
hidden_message = [
121, 111,117,
32, 115, 111,
108, 118, 101,
100, 32, 116,
104, 101, 32,
109, 97, 103,
105, 99, 32,
112, 117, 122,
122, 108, 101
]
# finish this lambda
decode = lambda a: "".join([chr(n) for n in a])
# should print the message
print(decode(hidden_message))


def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


if __name__ == '__main__':
    gen = fib()
    for _ in range(100):
        print(next(gen))

