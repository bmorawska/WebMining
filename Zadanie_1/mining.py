import pandas as pd
import uuid
from datetime import timedelta
from tqdm import tqdm


INPUT_FILE = 'data_full.csv'
session_timeout = timedelta(seconds=(30 * 60))  # 30 minut * 60 sekund
data = pd.read_csv(INPUT_FILE)
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y %H:%M:%S')

users = data.ip.unique()

users_sessions = []
for user in tqdm(users):
    session = None
    start = None
    end = None
    visited_pages = []
    for index, row in data.iterrows():
        if row.ip == user:
            if start is None:
                start = row.date
                end = start
                prev_end = start
            else:
                prev_end = end
                end = row.date

            if end - start > session_timeout:
                session = {
                            "user": user,
                            "sessionID": uuid.uuid1(),
                            "start_time": start,
                            "end_time": prev_end,
                            "visited_pages": visited_pages
                           }
                users_sessions.append(session)
                session = None
                visited_pages = []
                start = row.date
                end = start

            visited_pages.append(row.address)

    session = {
        "sessionID": uuid.uuid1(),
        "user": user,
        "start_time": start,
        "end_time": end,
        "visited_pages": visited_pages
    }
    users_sessions.append(session)


sessions = pd.DataFrame(users_sessions)
sessions.set_index('sessionID')
sessions.sort_values(by=['user'], inplace=True)
sessions.to_csv('sessions.csv', index=False)
