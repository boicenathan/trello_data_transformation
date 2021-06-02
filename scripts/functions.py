### Functions for the repo ###


# Creating the function to insert a row
def insert_row(df, my_row):
    df.loc[len(df)] = my_row


def timer(start, end):
    total = round(end - start, 0)

    if total < 60:
        print('\nProcess complete in', int(total), 'seconds')
    elif total > 60:
        mintot = total / 60
        sectot = (mintot - int(mintot)) * 60
        print('\nProcess complete in', int(mintot), 'minutes', int(sectot), 'seconds')
