 # -*- coding: utf-8 -*-
"""
File: utils.py
Created on Sun Apr 12 2020

@author: Ankit Bansal

=========================================================================
Most common functions which are used by any other project
=========================================================================
"""

import pandas as pd
import os
import sys
from pathlib import Path
from zipfile import ZipFile

def read_from_zip(zip_path):
    '''
    Given a zip file reads content of the file and returns dataframe
    This function supports csv, and Json files.
    Assumes that a single (zip) file has only 1 (pandas) readable file
    '''

    with ZipFile(zip_path, "r") as z:
        for file in z.namelist():
            if file.endswith('.csv'):
                with z.open(file) as f:
                    data = pd.read_csv(f)
            elif file.endswith('.json'):
                with z.open(file) as f:
                    data = pd.read_json(f)
            else:
                raise "No suitable file found"

    return data
