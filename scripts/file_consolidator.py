### Step 1: Consolidate All CSV's in a Sub Folder ###

import functions
from datetime import datetime
import pandas as pd
import glob
import time

path = ''

# Start timer
start = time.time()

# Get a list of all the paths
files = glob.glob(path + '/*/*.csv')
print(str(len(files)), 'files')

# Create the consolidated dataframe
print('Consolidating...')
data = (pd.read_csv(f, sep=',') for f in files)
merged_df = pd.concat(data, ignore_index=True)

# Saving file
merged_df.to_csv(path + '/Consolidated.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
today = datetime.now()
functions.timer(start, end, today)
