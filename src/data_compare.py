### Step 3: Compare Card ID Between Trello and Cognos ###

import numpy as np
import pandas as pd
import funcs.functions
import time
from datetime import datetime


def data_compare():
    # Start timer
    start = time.time()

    # Creating dataframes for the exported files
    trello_df = pd.read_csv('data/Trimmed.csv')
    df2 = pd.read_csv('data/CogTrimmed.csv')

    # Updating the Cognos df and adjusting the column names
    cog_df = df2[['Card Id', 'Squad', 'List Name']]
    cog_df.columns = ['card_id', 'squad_name', 'list_name_cog']

    # Doing the merge on card id
    new = pd.merge(trello_df, df2, on='card_id', how='left')

    # Checking if the list names match (can be changed to whatever data you want to check
    new['list_match'] = np.where(new.list_name == new.list_name_cog, 'Match', np.nan)

    # Saving the file
    new.to_csv('data/Matches.csv', index=False)

    # Stop timer and calculate runtime
    end = time.time()
    today = datetime.now()
    funcs.functions.timer(start, end, today)


if __name__ == '__main__':
    data_compare()
