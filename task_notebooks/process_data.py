from typing import List, Dict
from pathlib import Path

import pandas as pd

ARRESTS_KEY_COLS = [
	'Apprehension Date',
	'Apprehension State',
	'Apprehension AOR',
	'Final Program',
	'Apprehension Method',
	'Apprehension Criminality',
	'Case Status',
    'Case Category',
    'Departed Date',
    'Departure Country',
    'Final Order Yes No',
    'Birth Year',
    'Citizenship Country',
    'Gender',
    'Apprehension Site Landmark',
    'Unique Identifier']


def read_arrests_data(
    path: Path, 
    usecols: List[str] = ARRESTS_KEY_COLS,
    header_row: int = 6):
    """
    Read in arrests csv file into a dataframe. Cleans column names and string columns.
    inputs:
        path: path to the arrests file - can take .csv or .xlsx file of the data (see notes in README)
        usecols: columns to use (see 0-data_exploration.ipynb for reasoning on ARRESTS_KEY_COLS)
        header_row: index of the header row in the excel file
    returns:
        pandas DataFrame of the arrests data
    """
    arrests_df = pd.read_excel(path, usecols=usecols, header=header_row)

    arrests_df.columns = [x.strip().lower().replace(' ','_') for x in arrests_df.columns]
    for c in arrests_df.columns:
        if arrests_df[c].dtype == 'object' and c !='unique_identifier':
            arrests_df[c] = arrests_df[c].str.strip().str.upper()
    return arrests_df






