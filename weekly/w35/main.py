import random


def remove_duplicates(my_list: list) -> list:
    return list(set(my_list))


def chop(my_list: list) -> None:
    my_list.pop(0)
    my_list.pop(-1)


def middle(my_list: list) -> list:
    return my_list[1: -1]


if __name__ == '__main__':
    my_list = [random.randint(0, 5) for _ in range(100)]
    print(my_list)

    new_list = remove_duplicates(my_list)
    chop(new_list)
    print(new_list)
    print(middle(new_list))