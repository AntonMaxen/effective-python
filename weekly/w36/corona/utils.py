import json
import datetime
import os


def get_numbers(arr, my_list=[]):
    if not isinstance(arr, list):
        return my_list.append(arr)

    for v in arr:
        get_numbers(v, my_list)

    return my_list


def group_files(filenames, path):
    return {f.split('.')[0]: os.path.join(path, f) for f in filenames}


def get_json(file_name):
    return json.loads(open(file_name, mode='r').read())


def yearweek_to_date(x):
    return datetime.datetime.strptime(x + '-1', "%Y-W%W-%w")


def find_matches(a, b):
    return [[b_i for b_i, b_v in enumerate(b) if a_v == b_v] for a_i, a_v in enumerate(a)]


def save_json(obj, file_name):
    with open(file_name, mode='w+') as my_file:
        json.dump(obj, my_file, indent=4)
