### Card Count by Board ###

from datetime import date
import pandas as pd
import time
import functions

# Start timer
start = time.time()
today = str(date.today()).replace('-', '.')

# Load consolidated file
cons = pd.read_csv(functions.path + '/consolidated.csv', dtype=str, keep_default_na=False)
print('File loaded')

# Get a list of the board names
boards = list(cons['Board Name'].tolist())
boards_unique = set(boards)

# Creating a new df with board names
new = pd.DataFrame(columns=(['board_name', 'card_count']))

# Append to the df the count of cards per board
for i in boards_unique:
    ccount = boards.count(i)
    functions.insert_row(new, [i, ccount])

# Add a totals row and sort in descending order
new = new.sort_values('card_count', ascending=False)
ccount = new['card_count'].sum()
functions.insert_row(new, ['Total Cards', ccount])

# Saving file as consolidated
path = functions.path.replace('consolidated.csv', '')
new.to_csv(path + '/cards_count ' + str(today) + '.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
functions.timer(start, end)
