import pandas as pd
from random import sample, uniform


def shuffle_cols(df):
    return df[sample(list(df.columns.values), df.shape[1])]
def dirty_data(df):
    return (df.pipe(shuffle_cols) # Shuffle the columns
            .rename(lambda col: col.lower() if uniform(0, 1) < .25 else col, axis='columns') #randomly lower the value of column headers
            .rename(lambda col: '\'' + col + '\'' if uniform(0, 1) < .25 else col, axis='columns') #randomly encase column headers with quotes
            .update(df.sample(int(df.shape[1]/4), axis=1).applymap(str))) #randomly set numeric columns to string
