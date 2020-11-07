import numpy as np
import pandas as pd

INPUT_FILE = 'data_full.csv'
data = pd.read_csv(INPUT_FILE)
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y %H:%M:%S')

# Wyodrębnienie użytkowników i stron na jakie wchodzili do postaci <USER> [<SITES>]
data = data[['ip', 'address']]
data['sites'] = data.groupby(['ip']).transform(lambda x: ','.join(x))
data = data[['ip', 'sites']]
data['sites'] = data['sites'].apply(lambda x: x.split(','))
data.drop_duplicates(subset='ip', inplace=True, keep='first')
data.reset_index(drop=True, inplace=True)

# Analiza koszykowa
INPUT_FILE_MOST_POPULAR_SITES = 'percent_of_occurrences.csv'
sites = np.array(pd.read_csv(INPUT_FILE_MOST_POPULAR_SITES, usecols=[0]).values.tolist()).flatten()

cols = ['userID']
cols.extend(sites)
attributes = pd.DataFrame(columns=cols)
attributes['userID'] = data.ip
attributes.set_index('userID', inplace=True)

# Transformacja koszykowa
for col in cols:
    if col == 'userID':
        continue
    attributes[col] = 0

len_sites = len(sites)
for i, row in data.iterrows():
    vp = row.sites
    for site in vp:
        if site in sites:
            attributes.iloc[i][site] = 1

attributes.to_csv('user_attributes.arff', header=False)

header = '@RELATION user_attributes.arff\n\n' + \
         '@ATTRIBUTE userID STRING\n'

for site in sites:
    header += '@ATTRIBUTE ' + site + ' {0, 1}\n'

header += '\n\n@DATA\n'

with open('user_attributes.arff', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header.rstrip('\r') + '\n' + content)
