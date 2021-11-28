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