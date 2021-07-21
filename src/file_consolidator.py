### Consolidate All CSV's in a Sub Folder ###

import os.path
from funcs.functions import timer
import pandas as pd
import glob
from time import time


def file_consolidator():
    # Start timer
    start = time()

    # If the file should be split
    split = False

    # Sub-strings to exclude
    rboards = ['example', 'test', 'template', 'demo', 'butler', 'board', 'check', 'copy', 'do not use', 'asean',
               'benelux', 'ds&t', 'a2r']

    # Get a list of all the paths and base file names
    paths = glob.glob('data/boards/*/*.csv')
    files = [os.path.basename(x) for x in paths]

    # Filtering out boards with sub-strings from above and re-assembling paths
    newlst = [i for i in files if not any(r in i for r in rboards)]
    paths = ['data/boards/' + file.rsplit('.', 1)[0] + '/' + file for file in newlst]

    # Merging all the files
    print(f"Merging {len(newlst)} files, {len(files) - len(newlst)} filtered out")
    data = [pd.read_csv(p, sep=',') for p in paths]
    merged_df = pd.concat(data, ignore_index=True)

    # Saving the merged dataframe
    print(f"Saving {len(merged_df):,} rows")
    if split:  # Splitting the dataframe if indicated
        new1 = merged_df.iloc[:1000000, :]
        new2 = merged_df.iloc[1000001:, :]
        new1.to_csv('data/Consolidated1.csv', index=False, encoding='utf-8-sig')
        new2.to_csv('data/Consolidated2.csv', index=False, encoding='utf-8-sig')
    else:
        merged_df.to_csv('data/Consolidated.csv', index=False, encoding='utf-8-sig')

    # Stop timer and calculate runtime
    timer(start, "Merging")


if __name__ == '__main__':
    file_consolidator()
