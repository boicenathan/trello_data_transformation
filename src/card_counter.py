### Card Count by Board ###

from datetime import date, datetime
import pandas as pd
import time
import funcs.functions


def card_counter():
    # Start timer
    start = time.time()
    today = str(date.today()).replace('-', '.')

    # Load consolidated file
    cons = pd.read_csv('data/Consolidated.csv', dtype=str, keep_default_na=False)
    print('File loaded')

    # Get a list of the board names
    boards = list(cons['Board Name'].tolist())
    boards_unique = set(boards)

    # Creating a new df with board names
    new = pd.DataFrame(columns=(['board_name', 'card_count']))

    # Append to the df the count of cards per board
    for i in boards_unique:
        ccount = boards.count(i)
        funcs.functions.insert_row(new, [i, ccount])

    # Add a totals row and sort in descending order
    new = new.sort_values('card_count', ascending=False)
    ccount = new['card_count'].sum()
    funcs.functions.insert_row(new, ['Total Cards', ccount])

    # Saving file
    new.to_csv('data/Card_Count ' + str(today) + '.csv', index=False)

    # Stop timer and calculate runtime
    end = time.time()
    today = datetime.now()
    funcs.functions.timer(start, end, today)


if __name__ == '__main__':
    card_counter()
