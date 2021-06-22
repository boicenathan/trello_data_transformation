### Functions for the repo ###

path = ''


# Creating the function to insert a row
def insert_row(df, my_row):
    df.loc[len(df)] = my_row


# Creating a function to calculate the runtime of the script
def timer(start, end, today):
    total = round(end - start, 0)
    if total < 60:
        print('\nProcess complete in', int(total), 'seconds')
    elif total > 60:
        mintot = total / 60
        sectot = (mintot - int(mintot)) * 60
        now = str(today.strftime("%B %d, %Y %H:%M:%S"))
        print('Process complete in', int(mintot), 'minutes', int(sectot), 'seconds', 'on', str(now[:-9]), 'at', str(now[-8:]))
