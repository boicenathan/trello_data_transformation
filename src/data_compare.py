### Compare Data Between Two Data Sources ###

import numpy as np
import pandas as pd
from funcs.functions import timer
import time


def data_compare():
    # Start timer
    start = time.time()

    # Creating dataframes for the exported files
    trello_df = pd.read_csv('data/Trimmed.csv')
    df2 = pd.read_csv('data/OthTrimmed.csv')

    # Updating the Cognos df and adjusting the column names
    oth_df = df2[['Card Id', 'Squad', 'List Name']]
    oth_df.columns = ['card_id', 'squad_name', 'list_name_oth']

    # Doing the merge on card id
    new = pd.merge(trello_df, oth_df, on='card_id', how='left')

    # Checking if the list names match (can be changed to whatever data you want to check
    new['list_match'] = np.where(new.list_name == new.list_name_cog, 'Match', np.nan)

    # Saving the file
    new.to_csv('data/Matches.csv', index=False)

    # Stop timer and calculate runtime
    timer(start, "Trimming")


if __name__ == '__main__':
    data_compare()
