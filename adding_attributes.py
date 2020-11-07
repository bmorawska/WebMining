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
# attributes['user'] = "\"" + sessions['user'].astype(str) + "\""
# attributes['start_time'] = "\"" + sessions['start_time'].astype(str) + "\""
# attributes['end_time'] = "\"" + sessions['end_time'].astype(str) + "\""

# Kategoryzacja
session_time_categories = ['t<1min', '1min<=t<2min', '3min<=t<5min', '5min<=t<10min', '10min<=t<15min',
                           '15min<=t<30min']
session_time_ranges = [0, 1 * 60, 2 * 60, 5 * 60, 10 * 60, 15 * 60, 30 * 60]
attributes['session_time_categories'] = pd.cut(attributes['average_time'],
                                               session_time_ranges,
                                               labels=session_time_categories)

session_average_time_per_site_categories = ['t<1min', '1min<=t<2min', '2min<=t<5min', '5min<=t<30min']
session_average_time_ranges = [0, 1 * 60, 2 * 60, 5 * 60, 30 * 60]
attributes['session_average_time_per_site_categories'] = pd.cut(attributes['average_time'],
                                                                session_average_time_ranges,
                                                                labels=session_average_time_per_site_categories)

done_things_categories = ['x<=3', '3<=t<6', '6<=t<10', '10<=t<20', 'x>=20']
done_things_ranges = [0, 3, 6, 10, 20, 50]
attributes['done_things_categories'] = pd.cut(attributes['done_things'],
                                              done_things_ranges,
                                              labels=done_things_categories)

attributes.to_csv('session_attributes.arff', header=False)

header = '@RELATION session_attributes.arff\n\n' + \
         '@ATTRIBUTE sessionID STRING\n'

for site in sites:
    header += '@ATTRIBUTE ' + site + ' {0, 1}\n'

header += '@ATTRIBUTE session_time NUMERIC\n' + \
          '@ATTRIBUTE visited_sites NUMERIC\n' + \
          '@ATTRIBUTE avg_time_per_site NUMERIC\n' + \
          '@ATTRIBUTE session_time_categories {t<1min, 1min<=t<2min, 3min<=t<5min, 5min<=t<10min, ' \
          '10min<=t<15min, 15min<=t<30min}\n' + \
          '@ATTRIBUTE session_average_time_per_site_categories {t<1min, 1min<=t<2min, 2min<=t<5min, ' \
          '5min<=t<30min}\n' + \
          '@ATTRIBUTE done_things_categories {x<=3, 3<=t<6, 6<=t<10, 10<=t<20, x>=20}\n\n' + \
          '@DATA'

with open('session_attributes.arff', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header.rstrip('\r') + '\n' + content)
