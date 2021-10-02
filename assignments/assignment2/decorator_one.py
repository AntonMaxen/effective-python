import time
import sys

def lowercased(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return wrapper

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


@tired(2)
@lowercased
def name(n, f):
    return n + f




print(name('AnToN', 'fREDDAN'))
