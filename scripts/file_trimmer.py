### Step 2: Trim the File ###

import functions
import pandas as pd
import time

# Start timer
start = time.time()

# Load consolidated file
cons = pd.read_csv(functions.path + '/consolidated.csv', dtype=str, keep_default_na=False)
print('File loaded')

# Year to be extracted
year = ['2021']

# Creating a new df with only vital columns and cleaning the date field
new = cons[["Card ID", "Board Name", "List Name", "Last Activity Date"]].copy()
new.columns = ['card_id', 'board_name', 'list_name', 'last_activity']  # Renaming the columns to be easier to reference
new['last_activity'] = new['last_activity'].str[:10]  # Removing the time from the date
print('New df created')

# Lists to be INCLUDED
lists = ['Backlog - Bids', 'Backlog - Other', 'In Progress', 'In Progress - Bids', 'In Progress - Other',
         'Pending Input / Hand Offs', 'Issues and Blockers', 'Completed', 'Completed - Bids',
         'Completed - Other']

# Board sub strings to be EXCLUDED
boards = ['template', 'Template', 'Test', 'test', 'Example', 'example', 'do not use',
          'ASEAN', 'asean', 'Benelux', 'benelux', 'DS&T', 'A2R']

# Filtering the new dataframe by list, board, and date
new = new[new['list_name'].isin(lists)]  # Remove cards that are not in the lists variable
new['temp'] = new['board_name'].str.extract("(template|Template|Test|test|Example|example|do not use|ASEAN|asean|"
                                            "Benelux|benelux|DS&T|A2R)")  # Extracting sub strings to a new column
new = new[~new['temp'].isin(boards)]  # Removing the row if the board name is in the boards list
del new['temp']  # Removing the temporary column
new['year'] = new['last_activity'].str.extract("(2021)")  # Extracting the year 2021
new = new[new['year'].isin(year)]  # Removing rows that do not match the year variable value
del new['year']  # Removing the temporary column
print('Filtering done')

# Saving trimmed file
path = functions.path.replace('consolidated.csv', '')
new.to_csv(path + 'con_trimmed.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
functions.timer(start, end)
