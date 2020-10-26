import ast

import numpy as np
import pandas as pd

INPUT_FILE_SESSIONS = 'sessions_singles_removed.csv'
INPUT_FILE_MOST_POPULAR_SITES = 'percent_of_occurrences.csv'

sessions = pd.read_csv(INPUT_FILE_SESSIONS, usecols=['sessionID', 'user', 'start_time', 'end_time', 'visited_pages'])
sessions.set_index('sessionID', inplace=True)

sites = np.array(pd.read_csv(INPUT_FILE_MOST_POPULAR_SITES, usecols=[0]).values.tolist()).flatten()

cols = ['sessionID']
# cols.extend(sites)
attributes = pd.DataFrame(columns=cols)
attributes['sessionID'] = sessions.index
attributes.set_index('sessionID', inplace=True)

# Transformacja koszykowa
# for col in cols:
#    attributes[col] = False

# len_sites = len(sites)
# for i, row in sessions.iterrows():
#    vp = ast.literal_eval(row.visited_pages)
#    for site in vp:
#        if site in sites:
#            attributes.loc[i][site] = True

# Wyznaczanie czasu "sesji" w sekundach sensowny
sessions.end_time = pd.to_datetime(sessions.end_time)
sessions.start_time = pd.to_datetime(sessions.start_time)
attributes['sessionTime'] = (sessions.end_time - sessions.start_time).dt.seconds

# Timestamp ale nie wiem gdzie to ma być?
# first_log_time = pd.to_datetime('30-06-1995 20:00:01')
# sessions.end_time = pd.to_datetime(sessions.end_time)
# sessions.start_time = pd.to_datetime(sessions.start_time)
# attributes['sessionTime'] = ((sessions.end_time - first_log_time).dt.days * 24 * 60 * 60)

# Wyznaczanie liczby działań w czasie sesji
attributes['done_things'] = sessions.visited_pages
attributes['done_things'] = attributes['done_things'].apply(lambda x: len(ast.literal_eval(x)))

# Wyznaczanie przyciętnego czasu sesji
attributes['average_time'] = attributes['sessionTime'] / attributes['done_things']

pass
