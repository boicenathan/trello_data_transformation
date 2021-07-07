### Functions for the repo ###

# Creating the function to insert a row
def insert_row(df, my_row):
    df.loc[len(df)] = my_row


# Creating a function to calculate the runtime of the script
def timer(start, end, today):
    total = round(end - start, 0)
    now = str(today.strftime("%B %d, %Y %X %p"))
    if total < 60:
        print(f'Complete in {int(total)} seconds on {str(now[:-9])} at {str(now[-11:])}')
    elif total > 60:
        mintot = total / 60
        sectot = (mintot - int(mintot)) * 60
        print(f'Complete in {int(mintot)} minutes {int(sectot)} seconds on {str(now[:-12])} at {str(now[-11:])}')
