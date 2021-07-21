# Trello Data Transformation
## Initial setup
I recommend that you download [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) and use that to manage
this project. They have a great tutorial [here](https://www.jetbrains.com/help/pycharm/quick-start-guide.html#create) that
walks you through the process of setting up a project and installing Python. This code should work fine for Python >= 3.9

The project is located on GitHub [here](https://github.ibm.com/nboice/trello_data_transformation). You can either 
download the project or [clone it by connecting your GitHub to PyCharm](https://www.jetbrains.com/help/pycharm/github.html#register-account). 

Then add a folder named `src/data` in the project directory, and extract the downloaded zip folder from Trello into this `src/data` folder.  It should follow this format `src/data/boards`.

<img align="center" src="docs/datapath.PNG">

Now that you have all the files you need, create a fresh virtual environment for this project. Then, open PyCharm's terminal
interface and run the command `pip install -r config/requirements.txt`.

### Consolidator
By default after merging all the files it will save as one csv, but if you need to use it in Excel switch `split` to `True` and will split the dataframe at the 1 million row mark to fit within Excels visual loading limits.

`rboards` is the list of words we used when filtering.  If the board has any of these words in their name it will ignore the file.

### Trimmer
By default it filters out all rows with non-standards lists and cards with a date of last activity in 2021, but can change dramatically based on needs.

### Compare
By default this script compares the list name between Trello and Cognos just make sure the appropriate files are in the `data` folder.

### Count
This script will count the number of cards per board and then add a total row.
