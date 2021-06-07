### Step 2: Trim the File ###

import functions
import pandas as pd
import time

path = functions.path

# Start timer
start = time.time()

# Load consolidated file
cons = pd.read_csv(path + '/consolidated.csv', dtype=str, keep_default_na=False)
print('File loaded')

# Year to be extracted
year = ['2021']

# Creating a new df with only vital columns and cleaning the date field
new = cons[["Card ID", "Board Name", "List Name", "Last Activity Date"]].copy()
new.columns = ['card_id', 'board_name', 'list_name', 'last_activity']
new['last_activity'] = new['last_activity'].str[:10]
print('New df created')

# Lists to be included
lists = ['Backlog - Bids', 'Backlog - Other', 'In Progress', 'In Progress - Bids',
         'In Progress - Other', 'Pending Input / Hand Offs', 'Issues and Blockers',
         'Completed', 'Completed - Bids', 'Completed - Other']

# Board sub strings to be excluded
boards = ['template', 'test', 'example', 'do not use',
          'asean', 'benelux', 'ds&t', 'a2r', 'demo', 'butler', 'board', 'check', 'copy']

# Filtering the new dataframe by list, board, and date
new = new[new['list_name'].isin(lists)]
new['name_lower'] = new['board_name'].str.lower()
new['temp'] = new['name_lower'].str.extract("(template|test|example|do not use|asean|benelux|ds&t|a2r|demo|butler|board"
                                            "|check|copy)")
new = new[~new['temp'].isin(boards)]
new['year'] = new['last_activity'].str.extract("(2021)")
new = new[new['year'].isin(year)]

# Delete all the temporary columns
del new['temp']
del new['name_lower']
del new['year']
print('Filtering done')

# Saving trimmed file
path = path.replace('consolidated.csv', '')
new.to_csv(functions.path + '/con_trimmed.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
functions.timer(start, end)
