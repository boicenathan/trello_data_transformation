### Trim the Merged File ###

import pandas as pd
import funcs.functions
import time


def file_trimmer():
    # Start timer
    start = time.time()

    # Update rows 13 and 14 depending on needs
    year = ['2021']  # Year to be extracted
    cols = ['Card Id', 'Last Activity Date', 'Board Name', 'List Name']  # Columns to load from merged file

    # Loading in the merged file
    print("Loading file...")
    df = pd.read_csv('data/Consolidated.csv', usecols=cols, dtype=str)

    # Creating a new df with only vital columns and cleaning the date field
    df.columns = ['card_id', 'last_activity', 'board_name', 'list_name']
    print('New df created')

    # Lists to be included
    lists = ['Backlog - Bids', 'Backlog - Other', 'Completed', 'Completed - Bids', 'Completed - Other', 'In Progress',
             'In Progress - Bids', 'In Progress - Other', 'Issues and Blockers', 'Pending Input / Hand Offs']

    # Filtering the new dataframe by list and date
    print("Filtering...")
    df = df[df['list_name'].isin(lists)]
    df['last_activity'] = df['last_activity'].str[:10]
    df['year'] = df['last_activity'].str.extract("(2021)")
    df = df[df['year'].isin(year)]
    del df['year']  # Delete all the temporary columns

    # Saving the trimmed file
    print("Saving...")
    df.to_csv('data/Trimmed.csv', index=False)    # Saving trimmed file

    # Stop timer and calculate runtime
    funcs.functions.timer(start)


if __name__ == '__main__':
    file_trimmer()
