### Card Count by Board ###

from datetime import date
import pandas as pd
import time
import funcs.functions


def card_counter():
    # Start timer
    start = time.time()
    today = str(date.today().strftime("%y.%m.%d"))

    # Load consolidated file
    print("Loading...")
    data = pd.read_csv('data/Consolidated.csv', usecols='Board Name', dtype=str, keep_default_na=False)

    # Get full and unique lists of the board names
    boards = list(data['Board Name'].tolist())
    boards_unique = set(boards)

    # Creating a new df with board names
    df = pd.DataFrame(columns=(['board_name', 'card_count']))

    # Append to the df the count of cards per board
    for i in boards_unique:
        ccount = boards.count(i)
        funcs.functions.insert_row(df, [i, ccount])

    # Add a totals row and sort in descending order
    df = df.sort_values('card_count', ascending=False)
    ccount = df['card_count'].sum()
    funcs.functions.insert_row(df, ['Total Cards', ccount])

    # Saving file
    df.to_csv('data/Card_Count_' + today + '.csv', index=False)

    # Stop timer and calculate runtime
    funcs.functions.timer(start)


if __name__ == '__main__':
    card_counter()
