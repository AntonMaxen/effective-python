import numpy as np
def normalize_matrix(matrix: np.ndarray,
                     minimum: float, maximum: float) -> np.ndarray:

    return (matrix - minimum) / (maximum - minimum)


def test():
    records = cases.get('records')
    dates = [record.get('dateRep') for record in records]
    date_times = [datetime.datetime.strptime(d, '%d/%m/%Y') for d in dates]
    deaths = [record.get('deaths') for record in records]
    reshaped_deaths = np.reshape(np.array(deaths, dtype=np.uint32), (-1, 2))
    plt.imshow(reshaped_deaths)
    plt.show()
