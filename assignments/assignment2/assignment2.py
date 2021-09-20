from functools import reduce


def my_reduce(my_dict):
    new_list = []
    for key, d in my_dict.items():
        new_dict = {'name': key}
        new_dict = {**new_dict, **d}
        new_list.append(new_dict)

    return new_list


my_short_reduce = lambda my_dict: reduce(lambda a, b: [*a, {**b[1], 'name': b[0]}], my_dict.items(), [])


def main():
    my_dict = {
        "john": {
            "age": 32,
            "favourite_color": "pink"
        },
        "sarah": {
            "age": 22,
            "favourite_color": "red"
        },
        "hannah": {
            "age": 19,
            "favourite_color": "green"
        },
        "michael": {
            "age": 56,
            "favourite_color": "blue"
        },
        "david": {
            "age": 43,
            "favourite_color": "yellow"
        }
    }

    # print(f'result: {reduce(some, my_dict.items(), [])}')

    print(reduce(lambda a, b: [*a, {**b[1], 'name': b[0]}], my_dict.items(), []))


def some(acumulator, new_value):
    print(f'a: {acumulator}')
    print(f'b: {new_value}')
    return [*acumulator, {**new_value[1], 'name': new_value[0]}]


if __name__ == '__main__':
    main()
