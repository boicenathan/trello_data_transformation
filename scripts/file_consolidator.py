### Step 1: Consolidate All CSV's in a Sub Folder ###

import functions
import pandas as pd
import glob
import time

# Start timer
start = time.time()

files = glob.glob(functions.path + '/*/*.csv')
print(str(len(files)), 'files')

data = pd.DataFrame()

for count, f in enumerate(files, 1):
    csv = pd.read_csv(f, dtype=str, keep_default_na=False)
    data = data.append(csv)
    print(str(round(((count/len(files))*100), 2)) + '%' + ' (' + str(count) + ')')

data.to_csv(functions.path + '/consolidated.csv', index=False)

# Stop timer and calculate runtime
end = time.time()
timer(start, end)
