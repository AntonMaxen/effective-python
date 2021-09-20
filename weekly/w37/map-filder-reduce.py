import math
from functools import reduce
# 1.
power_of_two = lambda arr: [e ** 2 for e in arr]
map_power_of_two = lambda arr: map(lambda e: e ** 2, arr)

# 2.
greater_than_fifty = lambda arr: [e for e in arr if e > 50]
map_greater_that_fifty = lambda arr: filter(lambda e: e > 50, arr)

# 3.
glue = lambda arr: reduce(lambda a, b: {**a, **b}, arr)
gl = lambda arr: {key: dicts[key] for dicts in arr for key in dicts}


def main():
    my_list = [100, 1000, 3, 1, 60, 50, 7, 300, 49]
    print(greater_than_fifty(my_list))
    print(list(map_greater_that_fifty(my_list)))

    my_arr = [
        {
            "name": "john"
        },
        {
            "age": 33
        },
        {
            "favouriteColor": "yellow"
        }
    ]
    print(gl(my_arr))
    pass


if __name__ == '__main__':
    main()
