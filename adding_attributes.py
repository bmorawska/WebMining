import ast

import numpy as np
import pandas as pd

INPUT_FILE_SESSIONS = 'sessions_singles_removed.csv'
INPUT_FILE_MOST_POPULAR_SITES = 'percent_of_occurrences.csv'

sessions = pd.read_csv(INPUT_FILE_SESSIONS, usecols=['sessionID', 'user', 'start_time', 'end_time', 'visited_pages'])
sessions.set_index('sessionID', inplace=True)

sites = np.array(pd.read_csv(INPUT_FILE_MOST_POPULAR_SITES, usecols=[0]).values.tolist()).flatten()

cols = ['sessionID']
cols.extend(sites)
attributes = pd.DataFrame(columns=cols)
attributes['sessionID'] = sessions.index
attributes.set_index('sessionID', inplace=True)

# Transformacja koszykowa
for col in cols:
    if col == 'sessionID':
        continue
    attributes[col] = 0

len_sites = len(sites)
for i, row in sessions.iterrows():
    vp = ast.literal_eval(row.visited_pages)
    for site in vp:
        if site in sites:
            attributes.loc[i][site] = 1

# Wyznaczanie czasu "sesji" w sekundach sensowny
sessions.end_time = pd.to_datetime(sessions.end_time)
sessions.start_time = pd.to_datetime(sessions.start_time)
attributes['sessionTime'] = (sessions.end_time - sessions.start_time).dt.seconds

# Wyznaczanie liczby działań w czasie sesji
attributes['done_things'] = sessions.visited_pages
attributes['done_things'] = attributes['done_things'].apply(lambda x: len(ast.literal_eval(x)))

# Wyznaczanie przyciętnego czasu sesji
attributes['average_time'] = attributes['sessionTime'] / attributes['done_things']
attributes['user'] = "\"" + sessions['user'].astype(str) + "\""
attributes['start_time'] = "\"" + sessions['start_time'].astype(str) + "\""
attributes['end_time'] = "\"" + sessions['end_time'].astype(str) + "\""
attributes.to_csv('session_attributes.arff', header=False)

header = '@RELATION session_attributes.arff\n\n' + \
         '@ATTRIBUTE sessionID STRING\n'

for site in sites:
    header += '@ATTRIBUTE ' + site + ' {0, 1}\n'

header += '@ATTRIBUTE session_time NUMERIC\n' + \
          '@ATTRIBUTE visited_sites NUMERIC\n' + \
          '@ATTRIBUTE avg_time_per_site NUMERIC\n' + \
          '@ATTRIBUTE user STRING\n' + \
          '@ATTRIBUTE start_time DATE "yyyy-MM-dd HH:mm:ss"\n' + \
          '@ATTRIBUTE end_time DATE "yyyy-MM-dd HH:mm:ss"\n\n' + \
          '@DATA'

with open('session_attributes.arff', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header.rstrip('\r') + '\n' + content)
