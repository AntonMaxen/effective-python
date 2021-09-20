import datetime
import pathlib
import os
from utils import (
    group_files,
    get_json,
    yearweek_to_date,
    find_matches,
    save_json
)


def generate_data():
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

    case_data_to_check = [[case_countries[i], date] for i, date in enumerate(case_dates)]
    vac_data_to_check = [[vac_countries[i], date] for i, date in enumerate(vac_dates)]

    matches = find_matches(case_data_to_check, vac_data_to_check)
    vaccines = [[vac_records[i] for i in indices] for indices in matches]
    for i, _ in enumerate(case_records):
        case_records[i]['vaccines'] = vaccines[i]

    short_records = [case_records[i] for i, v in enumerate(vaccines) if v]
    print(len(case_records))
    print(len(short_records))

    #save_json(short_records, files['result'])


if __name__ == '__main__':
    generate_data()
