"""Helper functions for signal_at_orf"""

import pandas as pd
import os
import time
from colorama import Fore, Back, Style


def print_elapsed_time(t0):
    """
    Given a start time (time.time() object), computes and prints time elapsed
    since then.

    Keyword arguments:
    :param start_time: Start time to compute elapsed time from (no default)
    :return: Pandas data frame concatenating all read files
    """
    elapsed_time = time.time() - t0
    if elapsed_time < 60:
        print(Fore.YELLOW + "Completed in {:2.1f} sec.".format(elapsed_time))
    elif 60 < elapsed_time < 3600:
        print(Fore.YELLOW + "Completed in {:2.1f} min.".format(elapsed_time / 60))
    else:
        print(Fore.YELLOW + "Completed in {:2.1f} hr.".format(elapsed_time / 3600))


def get_filename_from_path(inputFile):
    """
    Given a path to a file, gets the filename as a string.
    
    Keyword arguments:
    :param inputFile: path to a file (no default)
    :return: Tuple of strings: complete file name and name without the extension
    """
    dirname = os.path.dirname(inputFile)
    filename = os.path.basename(inputFile)
    extless_filename = os.path.basename(os.path.splitext(inputFile)[0])
    return dirname, filename, extless_filename


def rotate_table(df):
    """
    Given a pandas dataframe, rotates values 180 degrees (keeping indices).
    
    Keyword arguments:
    :param df: pandas dataframe (no default)
    :return: rotated pandas dataframe
    """

    # Flip rows
    flipped_df = df.copy()
    row_count = len(df.index)
    loop_i = 1
    for row in df.iterrows():
        index = row_count - loop_i
        flipped_df.iloc[index, :] = row[1].values
        loop_i += 1
    
    # Flip columns
    rotated_df = flipped_df.copy()
    column_count = len(flipped_df.columns)
    loop_i = 0
    for column in flipped_df:
        index = column_count - loop_i
        rotated_df[index] = flipped_df[column]
        loop_i += 1
    
    print('Rotated table 180 degrees.')
    return rotated_df


def rectangular_to_tidy(df, barcode):
    """
    Given a pandas dataframe, adapts it to tidy format (one variable per column).
    
    Keyword arguments:
    :param df: pandas dataframe (no default)
    :param barcode: plate barcode (no default)
    :return: pandas dataframe in tidy format
    """

    tidy_df = pd.DataFrame()
    
    for col in df.columns:
        for index in df.index:
            temp = pd.DataFrame({'Barcode': barcode, 'Well': str(index)+str(col), '440': df.loc[index,col]},
                                index=[0])
            tidy_df = pd.concat([tidy_df, temp])
    
    # Reorder columns
    tidy_df = tidy_df[['Barcode', 'Well', '440']]
    
    print('Put table in tidy (vertical) format.')
    return tidy_df
