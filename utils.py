import pandas as pd
import numpy as np
from random import sample, uniform
import sqlite3
from sqlite3 import Error


# def shuffle_cols(df: pd.DataFrame):
#     return df[sample(list(df.columns.values), df.shape[1])]


def some_numeric_to_str(df: pd.DataFrame):
    df.update(df.sample(int(df.shape[1]/4), axis=1).applymap(str))
    return df

def int_all(df):
    for col in df:
        try:
            df[col] = df[col].apply(int)
        except:
            pass
    return df

def duplicate_df_poorly(df: pd.DataFrame, dup_n: int = 2):
    return pd.concat([df]+[df.mask(np.random.random(df.shape) < .1)]*dup_n)


def dirty_data(df: pd.DataFrame):
    return (df.sample(frac=1, axis=1)  # Shuffle the columns
            # randomly lower the value of column headers
            .rename(lambda col: col.upper() if uniform(0, 1) < .25 else col, axis='columns')
            # randomly encase column headers with quotes
            .rename(lambda col: '\'' + col + '\'' if uniform(0, 1) < .25 else col, axis='columns')
            # randomly set numeric columns to string
            .pipe(some_numeric_to_str)
            # Duplicate the rows (students will know that ID's are unique)
            .pipe(duplicate_df_poorly)
            .sample(frac=1)
            )


def create_connection(db_file: str):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn


def make_db(df_path: str):
    """For the df at the given path, dirty the data and generate a db containing the dirty data

    Args:
        df_path (str): path to DataFrame data (in a CSV)
    """
    conn = create_connection('hw.db')
    df = dirty_data(pd.read_csv(df_path))
    df.to_sql('df', con=conn, if_exists='replace')


def generate_data():
    make_db('baseball_data.csv')

def undo_everything(db_path:str) -> pd.DataFrame:
    """For a db path, get back the original data

    Args:
        db_path (str): path to a DB with an unclean table

    Returns:
        pd.DataFrame: the original (clean) data
    """
    conn = sqlite3.connect(db_path)
    df = (pd.read_sql("SELECT * FROM df", con=conn)
        .drop('index', axis=1)
        .rename(lambda col: col.strip('\''), axis='columns')
        .rename(lambda col: col.upper(), axis='columns')
        .drop_duplicates(subset=['ID'])
        .apply(int_all)
        )
    print(df)
    return df

if __name__ == "__main__":
    generate_data()
    df = pd.read_csv('baseball_data.csv')
    # print(df)
    # print(df.equals(undo_everything('hw.db')))