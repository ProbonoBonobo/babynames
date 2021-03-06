# babynames
A simple Flask application to visualize the popularity of various baby names in the United States over time.

___

## Task 1: Installing dependencies
This starter template uses a Python dependency manager called `poetry`, which is a convenient way to manage Python dependencies in an automatically-generated virtual environment. To install `poetry`, run the following command:

```bash
pip install poetry
```

Once installed, you should be able to install the project locally with:

```bash
poetry install
```

Once installed, we can activate the virtual environment with:

```bash
poetry shell
```

Verify that the virtual environment is active by running:

```bash
which python 
```

This should something like `~/projects/babynames/.venv/bin/python` to your console, depending on where you installed the repository.

## Task 2: 

In the `babynames/datasets` directory, you'll find a `database.sqlite` file that contains 2 tables: `national` and `states`. These tables are derived from the Kaggle "US Baby Names" dataset [available here](https://www.kaggle.com/kaggle/us-baby-names).

For the purpose of this project, we'll be using the `national` table. This is loaded in the `babynames/manage.py` file. Head over to that file and examine the `hello` endpoint. You should be able to execute this method by running `python manage.py hello` inside the babynames directory.

## Task 3

Once we've verified that we can run the 'hello' method, we can start exploring the data. Our objective will be to plot a timeseries of the number of babynames born per year for each year in the range 1880-2014 (the last year on record). In order to plot this, we'll need a python object that contains baby counts for *each* of the years on record -- whether or not the name was actually born in that year. 

This might be easiest to do by creating a dictionary of dictionaries, where the outer dictionary is indexed by the name, and the inner dictionary is indexed by the year, so that we can store the counts for each name in each year. This might look something like:

```python3
d = {
        "John" : {
                1880: 0,
                1881: 13,
                1882: 24,
                # and so on...
                2014: 232982
        }
}
```

Try your hand at this! First create a SQL query that returns a flat list of records for all babies named "Tequila" for each year on record, then try to construct a dictionary object with the number of babies named "Tequila" for each year.

### Pro Tip
Have a look at a brilliant little datastructure called a `defaultdict`: this is a dictionary that will automatically create a new key if it doesn't already exist. It works like this:

```python3
# import the defaultdict
from collections import defaultdict # this is actually a built-in Python module, not a third-party library, so no installation of anything required. And because it's part of the standard library, you can use it in programming interviews!
data = {2013: 5, 2014: 10}
d = defaultdict(int, data)
print(d[1880]) # prints the result of calling `int()` with no argument -- e.g., 0
print(d[2013]) # prints the value of the dictionary we passed when initializing the defaultdict -- e.g., 5

```