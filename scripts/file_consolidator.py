### Step 1: Consolidate All CSV's in a Sub Folder ###

import functions
from datetime import datetime
import pandas as pd
import glob
import time

path = functions.path
rowsplit = 652578

# Start timer
start = time.time()

# Get a list of all the paths
files = glob.glob(path + '/*/*.csv')
print(str(len(files)), 'files')

# Create the consolidated dataframe
print('Consolidating...')
data = (pd.read_csv(f, sep=',') for f in files)
merged_df = pd.concat(data, ignore_index=True)

if len(merged_df.index) > 1000000:
    new1 = merged_df.iloc[:rowsplit, :]
    rowsplit = rowsplit + 1
    new2 = merged_df.iloc[rowsplit:, :]
    # Saving files
    new1.to_csv(path + '/Consolidated1.csv', index=False)
    new2.to_csv(path + '/Consolidated2.csv', index=False)
else:
    # Saving file
    merged_df.to_csv(path + '/Consolidated.csv', index=False)

# If total rows is over 1.4m but analysis still needs to be done we need to save this dataframe
alldata = data

# Stop timer and calculate runtime
end = time.time()
today = datetime.now()
functions.timer(start, end, today)
