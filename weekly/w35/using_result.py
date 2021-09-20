import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


def main():
    result = json.loads(open('result.json').read())
    print(len(result))
    sweden_data = [r for r in result if r.get('geoId') == 'SE']

    #x_axis = [sum([int(vaccine.get('NumberDosesReceived') or 0) for vaccine in report['vaccines']]) for report in sweden_data]
    dates = [record.get('dateRep') for record in sweden_data]
    time_stamps = [datetime.datetime.strptime(d, '%d/%m/%Y').date() for d in dates]
    print(time_stamps)
    x_axis = time_stamps
    y_axis = [report.get('deaths') for report in sweden_data]
    print(len(x_axis))
    print(len(y_axis))
    print(y_axis)

    fig, ax = plt.subplots()
    ax.scatter(x_axis, y_axis)

    ax.set(xlabel='Doses', ylabel='Deaths', title='Doses & Deaths')
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main()
