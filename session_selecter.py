import pandas as pd

INPUT_FILE = 'sessions.csv'
sessions_all = pd.read_csv(INPUT_FILE)  # single sites are loaded too
sessions = sessions_all[sessions_all['start_time'] != sessions_all['end_time']]

sessions.to_csv('sessions_singles_removed.csv')
