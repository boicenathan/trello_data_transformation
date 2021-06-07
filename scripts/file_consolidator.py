### Step 1: Consolidate All CSV's in a Sub Folder ###

import functions
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

# Create the dataframe and open them one by one and append them to the df
data = pd.DataFrame()

for count, f in enumerate(files, 1):
    csv = pd.read_csv(f, dtype=str, keep_default_na=False)
    data = data.append(csv)
    print(str(round(((count/len(files))*100), 2)) + '%' + ' (' + str(count) + ')')

if len(data.index) > 1000000:
    new1 = data.iloc[:rowsplit, :]
    rowsplit = rowsplit + 1
    new2 = data.iloc[rowsplit:, :]
    new1.to_csv(path + '/consolidated1.csv', index=False)
    new2.to_csv(path + '/consolidated2.csv', index=False)
else:
    # Save the consolidated file
    data.to_csv(path + '/consolidated.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
functions.timer(start, end)
