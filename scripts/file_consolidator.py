### Step 1: Consolidate All CSV's in a Sub Folder ###

import functions
import pandas as pd
import glob
import time

# Start timer
start = time.time()

# Storing all the file paths in the sub directory
files = glob.glob(functions.path + '/*/*.csv')
print(str(len(files)), 'files')

# Creating the dataframe
data = pd.DataFrame()

# Open each CSV in the sub directory, append the data to the dataframe, and print the progress
for count, f in enumerate(files, 1):
    csv = pd.read_csv(f, dtype=str, keep_default_na=False)
    data = data.append(csv)
    print(str(round(((count/len(files))*100), 2)) + '%' + ' (' + str(count) + ')')

# Save the dataframe to a CSV
data.to_csv(functions.path + '/consolidated.csv', index=False)

# Stop timer, calculate and print runtime
end = time.time()
functions.timer(start, end)
