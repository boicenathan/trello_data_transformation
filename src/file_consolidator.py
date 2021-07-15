### Consolidate All CSV's in a Sub Folder ###

import os
import funcs.functions
import pandas as pd
import glob
import time


def file_consolidator():
    # Start timer
    start = time.time()

    # Update rows 15 and 16 if needed
    split = False  # If the file should be split
    rboards = {'board', 'butler', 'check', 'copy', 'demo', 'do not use', 'example', 'template', 'test'}
    # ^^^ Keywords for boards to exclude ^^^

    # Get lists of paths and filenames
    paths = glob.glob('data/boards/*/*.csv')
    files = [os.path.basename(x) for x in paths]

    # Filtering out boards where filename contains any of the rboards strings and reassembling paths
    newlst = [i for i in files if not any(r in i for r in rboards)]
    paths = ['data/boards/' + file.rsplit('.', 1)[0] + '/' + file for file in newlst]

    # Create the consolidated dataframe
    print(f"Loading and merging {len(newlst)} files...")
    data = (pd.read_csv(p, sep=',') for p in paths)
    merged_df = pd.concat(data, ignore_index=True)

    # Splitting the files if needed to work in Excel
    print("Saving...")
    if split:
        rowsplit = 650000
        new1 = merged_df.iloc[:rowsplit, :]
        rowsplit += 1
        new2 = merged_df.iloc[rowsplit:, :]
        # Saving files
        new1.to_csv('data/Consolidated1.csv', index=False)
        new2.to_csv('data/Consolidated2.csv', index=False)
    else:
        # Saving to one file
        merged_df.to_csv('data/Consolidated.csv', index=False)

    # Stop timer and calculate runtime
    funcs.functions.timer(start)


if __name__ == '__main__':
    file_consolidator()
