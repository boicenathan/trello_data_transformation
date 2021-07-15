### Compare Data Between Files ###

import numpy as np
import pandas as pd
import funcs.functions
import time


def data_compare():
    # Start timer
    start = time.time()

    # Columns to use from other file
    cols = ['Card Id', 'Board', 'List Name']

    # Creating dataframes for the exported files
    print("Loading files...")
    trello_df = pd.read_csv('data/Trimmed.csv')
    df2 = pd.read_csv('data/OthTrimmed.csv', usecols=cols)

    # Updating column names, merging, and comparing
    print("Transforming...")
    df2.columns = ['card_id', 'squad_name', 'list_name_oth']
    new = pd.merge(trello_df, df2, on='card_id', how='left')  # Merging on card id
    new['list_match'] = np.where(new.list_name == new.list_name_oth, 'Match', np.nan)  # Checking match

    # Saving the file
    print("Saving...")
    new.to_csv('data/Matches.csv', index=False)

    # Stop timer and calculate runtime
    funcs.functions.timer(start)


if __name__ == '__main__':
    data_compare()
