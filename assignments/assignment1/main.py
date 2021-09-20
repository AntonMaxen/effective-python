def mult_sum(arr):
    tot = 0
    for i, v in enumerate(arr):
        if isinstance(v, list):
            tot += sum(v)
        else:
            tot += v

    return tot


def get_numbers(arr, my_list=[]):
    if not isinstance(arr, list):
        return my_list.append(arr)

    for v in arr:
        get_numbers(v, my_list)

    return sum(my_list)


def gcd_long(a, b):
    l, s = (a, b) if a > b else (b, a)
    matches = [i for i in range(s, 0, -1) if l % i == 0 and s % i == 0]
    return matches[0] if len(matches) > 0 else matches


def to_str(num, base):
    tot_string = ''
    while num > 0:
        remainder = num % base
        tot_string += str(remainder)
        num = num // base

    return tot_string


def main():
    pass


if __name__ == '__main__':
    main()
