import numpy as np
import pathlib
import os
import utils as u


def main():
    current_dir = pathlib.Path().resolve()
    data_path = os.path.join(current_dir, 'indata')
    filenames = ['cases.json', 'vaccines.json', 'result.json']
    files = u.group_files(filenames, data_path)
    result = u.get_json(files['result'])
    for r in result:
        if r['geoId'] == 'AT':
            print(r['vaccines'][0])


if __name__ == '__main__':
    main()
