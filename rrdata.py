#!/usr/bin/env python
import os
import time

import pandas as pd
from sodapy import Socrata
# [TODO] Add comments and explanation of how to get DOT_APP_TOKEN
# [TODO] future parameters
LIMIT_DAYS = 1000 * 60 * 24 * 7
IN_FILE_PATH = 'accident.pickle'
APP_TOKEN = os.getenv('DOT_APP_TOKEN')
OUT_FILE_PATH = 'accident.pickle'

results_df = None

# check if pickle file exists and within time limit
if os.path.exists(IN_FILE_PATH) and (time.time() - os.path.getmtime(IN_FILE_PATH) <= LIMIT_DAYS):
    results_df = pd.read_pickle(IN_FILE_PATH, compression='gzip')
else:
    client = Socrata("data.transportation.gov", APP_TOKEN)
    results = client.get("85tf-25kj", limit=1000000)
    results_df = pd.DataFrame.from_records(results)
    results_df.to_pickle(OUT_FILE_PATH, compression='gzip')