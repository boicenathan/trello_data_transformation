### Trim the File ###
import pandas as pd
from funcs.functions import timer
from time import time


def file_trimmer():
    # Start timer
    start = time()

    # Columns to use from merged file
    cols = ("Card ID", "Last Activity Date", "List Name", "Board Name")

    # Lists to be included
    lists = ['Backlog - Bids', 'Backlog - Other', 'Completed', 'Completed - Bids', 'Completed - Other', 'In Progress',
             'In Progress - Bids', 'In Progress - Other', 'Issues and Blockers', 'Pending Input / Hand Offs']

    # Start and end date for filter
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    # Loading merged file and updating column names
    print("Loading merged file")
    df = pd.read_csv('data/Consolidated.csv', usecols=cols)
    df.columns = ['card_id', 'last_activity', 'list_name', 'board_name']

    # Filtering the dataframe by list and date
    print("Filtering")
    df = df[df['list_name'].isin(lists)]  # Only keeping the row if the list is in lists
    df['last_activity'] = pd.to_datetime(df['last_activity']).apply(lambda x: x.strftime('%Y-%m-%d'))
    date_range = (df['last_activity'] >= start_date) & (df['last_activity'] <= end_date)
    df = df.loc[date_range]

    # Saving trimmed file
    print(f"Saving {len(df):,} rows")
    df.to_csv('data/Trimmed.csv', index=False)

    # Stop timer and calculate runtime
    timer(start, "Trimming")


if __name__ == '__main__':
    file_trimmer()
