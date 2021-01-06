import pandas as pd
from collections import Counter


def jacquard(A: list, B: list) -> float:
    nom = list(set(A).intersection(B))
    denom = list(dict.fromkeys(A + B))
    val = float(len(nom)) / float(len(denom))
    return val


# Ustawienia

THRESHOLD = 0.2
NUMBER_OF_SITES_TO_RECOMMEND = 10

# szukamy takich par <USER> [<VISITED SITES>]
data = pd.read_csv('data_full.csv')
data = data[['ip', 'address']]
data['sites'] = data.groupby(['ip']).transform(lambda x: ','.join(x))
data = data[['ip', 'sites']]
data['sites'] = data['sites'].apply(lambda x: x.split(','))
data.drop_duplicates(subset='ip', inplace=True, keep='first')
data.reset_index(drop=True, inplace=True)

# tworzymy nowego uzytkownia
jack_ip = 'Jack.Strong'
jack_sites = [
    '/shuttle/countdown/',
    '/shuttle/missions/sts-71/images/images.html',
    '/shuttle/missions/sts-71/mission-sts-71.html',
    '/shuttle/missions/sts-71/sts-71-info.html',
    '/facilities/mlp.html',
    '/shuttle/technology/sts-newsref/sts-av.html',
    '/history/apollo/apollo-13/sounds/a13_005.wav',
    '/shuttle/missions/sts-49/mission-sts-49.html',
    '/history/apollo/a-002/a-002.html',
    '/history/apollo/sa-6/sa-6.html'
]
size = data.shape[0]

data['sim'] = data['sites'].apply(lambda x: jacquard(list(dict.fromkeys(x)), jack_sites))
data.sort_values(by=['sim'], inplace=True, ascending=False)

data = data[data['sim'] >= THRESHOLD]
print(f'Rozmiar grupy z podobienstwem na poziomie {THRESHOLD} lub wiekszym: '
      f'{round(((data.shape[0]) / float(size) * 100), 2)}%\n')

recommended_sites = []
for _, row in data.iterrows():
    for site in row['sites']:
        if len(recommended_sites) == NUMBER_OF_SITES_TO_RECOMMEND:
            break
        if (site not in jack_sites) and (site not in recommended_sites):
            recommended_sites.append(site)

recommended_sites = Counter(recommended_sites).most_common()
if len(recommended_sites) >= NUMBER_OF_SITES_TO_RECOMMEND:
    recommended_sites = recommended_sites[: NUMBER_OF_SITES_TO_RECOMMEND]

print(f'Strony proponowane dla {jack_ip}:')
for idx, site in enumerate(recommended_sites):
    print(f'{idx + 1}. {site[0]}')
