import json
import datetime


cases = json.loads(open('cases.json').read())
vaccine = json.loads(open('vaccine.json').read())
yearweek_to_date = lambda x: datetime.datetime.strptime(x + '-1', "%Y-W%W-%w")


def main():
    records = cases.get('records')
    dates = [record.get('dateRep') for record in records]
    dates_case = [datetime.datetime.strptime(d, '%d/%m/%Y') for d in dates]
    country_case = [d['geoId'] for d in records]
    records_vac = vaccine.get('records')
    dates_vac = [yearweek_to_date(record.get('YearWeekISO')) for record in records_vac]
    country_vac = [v['Region'] for v in records_vac]

    data_to_check0 = list(map(lambda dat: [dat[1], country_case[dat[0]]], enumerate(dates_case)))
    data_to_check = list(map(lambda dat: [dat[1], country_vac[dat[0]]], enumerate(dates_vac)))

    for i, d in enumerate(data_to_check0):
        indices = [d_i for d_i, dv in enumerate(data_to_check) if d[0] == dv[0] and d[1] == dv[1]]
        vaccines = [records_vac[r_i] for r_i in indices]
        records[i]['vaccines'] = vaccines

    with open('result.json', mode='w+') as my_file:
        json.dump(records, my_file)


if __name__ == '__main__':
    main()
