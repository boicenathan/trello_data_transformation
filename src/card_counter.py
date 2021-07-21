### Card Count by Board ###

from datetime import date
import pandas as pd
from time import time
from funcs.functions import timer, insert_row
from collections import Counter


def card_counter():
    # Start timer
    start = time()
    today = str(date.today().strftime('%y.%m.%d'))

    # Load consolidated file
    cons = pd.read_csv('data/Consolidated.csv', usecols=["Board Name"], dtype=str, keep_default_na=False)
    print('File loaded')

    # Get a list of a list of all the boards, count cards, and convert dictionary to dataframe
    boards = cons['Board Name'].tolist()
    card_count = Counter(boards)
    df = pd.DataFrame(list(card_count.items()), columns=['Board', 'Card_Count'])

    # Add a totals row and sort in descending order
    df.sort_values('Card_Count', ascending=False, inplace=True)
    ccount = df['Card_Count'].sum()
    insert_row(df, ['Total Cards', ccount])

    # Saving file
    df.to_csv('data/Card_Count ' + today + '.csv', index=False)

    # Stop timer and calculate runtime
    timer(start, "Counting")


if __name__ == '__main__':
    card_counter()
