### Functions for the repo ###

from time import time, asctime, localtime


def insert_row(df, my_row):
    """ Function to insert a row to a dataframe. """
    df.loc[len(df)] = my_row


def timer(start, process):
    """ Timer to calculate program runtime. """
    total = time() - start
    if total < 60:
        print(f"{process} complete in {round(total, 0)} seconds on {asctime(localtime())}")
    elif total > 60:
        print(f"{process} complete in {round(total / 60, 0)} minutes "
              f"{round(((total / 60) - round(total / 60, 0)) * 60, 0)} seconds on {asctime(localtime())}")
