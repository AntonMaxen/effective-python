import json
import datetime


cases = json.loads(open('cases.json').read())
vaccine = json.loads(open('vaccine.json').read())
yearweek_to_date = lambda x: datetime.datetime.strptime(x + '-1', "%Y-W%W-%w")
get_week = lambda x: x.isocalendar()[1]


def main():
    records = cases.get('records')
    dates = [record.get('dateRep') for record in records]
    dates_case = [datetime.datetime.strptime(d, '%d/%m/%Y') for d in dates]
    records_vac = vaccine.get('records')
    dates_vac = [yearweek_to_date(record.get('YearWeekISO')) for record in records_vac]

    for i, d in enumerate(dates_case):
        indices = [d_i for d_i, dv in enumerate(dates_vac) if d == dv]
        vaccines = [records_vac[r_i] for r_i in indices]
        print(len(vaccines))
        records[i]['vaccines'] = vaccines

    amount = len([r['vaccines'] for r in records if len(r['vaccines']) > 0])
    print(amount)

    with open('result.json', mode='w+') as my_file:
        json.dump(records, my_file, indent=4)


if __name__ == '__main__':
    main()
