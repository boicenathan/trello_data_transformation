### Step 2: Trim the File ###

from functions import *
import pandas as pd
import time
from file_consolidator import path

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
lists = ['Backlog - Bids', 'Backlog - Other', 'In Progress', 'In Progress - Bids', 'In Progress - Other',
         'Pending Input / Hand Offs', 'Issues and Blockers', 'Completed', 'Completed - Bids',
         'Completed - Other']

# Board sub strings to be excluded
boards = ['template', 'Template', 'Test', 'test', 'Example', 'example', 'do not use',
          'ASEAN', 'asean', 'Benelux', 'benelux', 'DS&T', 'A2R']

# Filtering the new dataframe by list, board, and date
new = new[new['list_name'].isin(lists)]
new['temp'] = new['board_name'].str.extract("(template|Template|Test|test|Example|example|do not use|ASEAN|asean|"
                                            "Benelux|benelux|DS&T|A2R)")
new = new[~new['temp'].isin(boards)]
del new['temp']
new['year'] = new['last_activity'].str.extract("(2021)")
new = new[new['year'].isin(year)]
print('Filtering done')

# Saving trimmed file
path = path.replace('consolidated.csv', '')
new.to_csv(path + 'con_trimmed.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
timer(start, end)
