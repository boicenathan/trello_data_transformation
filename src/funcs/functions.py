### Functions  ###
import time


# Creating the function to insert a row
def insert_row(df, my_row):
    df.loc[len(df)] = my_row


# Creating a function to calculate the runtime of the script
def timer(start):
    end = time.time()
    total = round(end - start, 0)
    now = time.asctime(time.localtime())
    if total < 60:
        print(f"Complete in {int(total)} seconds at {now}")
    elif total > 60:
        mintot = total / 60
        sectot = (mintot - int(mintot)) * 60
        print(f"Complete in {int(mintot)} minutes {int(sectot)} seconds at {now}")
