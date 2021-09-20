def list_count(my_list: list) -> dict:
    my_dict = {}
    for c in my_list:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1

    return my_dict


def format_list_with_occurrence(my_list, my_dict):
    c_list = my_list.copy()

    for k, v in my_dict.items():
        count = 1
        while count <= v:
            for i, c in enumerate(c_list):
                if c == k:
                    c_list[i] = f'{c}-{count}'
                    count += 1

    return c_list


def main():
    my_list = ['z', 'i', 'f', 'q', 'i', 'o', 'k', 'x', 'w', 'g', 'p', 't', 'n', 'a', 's', 'j', 'r', 'b', 'w', 'i', 'k',
               'u', 'x', 'y']

    my_dict = list_count(my_list)
    c_list = format_list_with_occurrence(my_list, my_dict)

    print(c_list)


if __name__ == '__main__':
    main()