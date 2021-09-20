import json
import datetime
import pathlib
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
    all_matches = []
    for a_i, a_v in enumerate(a):
        all_matches.append([b_i for b_i, b_v in enumerate(b) if a_v == b_v])

    return all_matches


def is_match(a, b):
    pass



def main():
    current_dir = pathlib.Path().resolve()
    data_path = os.path.join(current_dir, 'indata')
    filenames = ['cases.json', 'vaccines.json', 'result.json']
    files = group_files(filenames, data_path)
    cases = get_json(files['cases'])
    vaccines = get_json(files['vaccines'])


    case_records = cases.get('records')
    case_dates = [datetime.datetime.strptime(r.get('dateRep'), '%d/%m/%Y') for r in case_records]
    case_countries = [r['geoId'] for r in case_records]

    vac_records = vaccines.get('records')
    vac_countries = [r['Region'] for r in vac_records]
    vac_dates = [yearweek_to_date(record.get('YearWeekISO')) for record in vac_records]

    case_data_to_check = [[date, case_countries[i]] for i, date in enumerate(case_dates)]
    vac_data_to_check = [[date, vac_countries[i]] for i, date in enumerate(vac_dates)]

    matches = find_matches(case_data_to_check, vac_data_to_check)
    vaccines = [[vac_records[i] for i in indices] for indices in matches]
    for i, _ in enumerate(case_records):
        case_records[i]['vaccines'] = vaccines[i]



    """
    for i, c_v in enumerate(case_data_to_check):
        v_indices = [v_i for v_i, v_v in enumerate(vac_data_to_check) if c_v[0] == v_v[0] and c_v[1] == v_v[1]]
        vaccines = [vac_records[v_i] for v_i in v_indices]
        case_records[i]['vaccines'] = vaccines

    with open(files['result'], mode='w+') as my_file:
        json.dump(case_records, my_file, indent=4)
    """


if __name__ == '__main__':
    main()
