import numpy as np
from sklearn.metrics import jaccard_score


def random_user_generator(allPagesLength: int, probability: float):
    visited = []
    for i in range(allPagesLength):
        num = np.random.uniform(0.0, 1.0)
        if num < probability:
            visited.append(0)
        else:
            visited.append(1)
    return visited


with open('pages.txt', 'r') as pages_file:
    pages = pages_file.readlines()

pages = list(map(lambda x: x[:-1], pages))

jack_ip = 'Jack.Strong'
# jack_visited = random_user_generator(len(pages), 0.7)
jack_visited = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]

print(f"{jack_ip}: {jack_visited}")

with open('clusters.txt', 'r') as clusters_file:
    lines = clusters_file.readlines()

clusters = []
for idx, line in enumerate(lines):
    if 'Cluster ' in line:
        clusters.append(list(map(int, lines[idx + 1].split(' ')[-28:])))

jaccard_scores = []
for i in range(len(clusters)):
    js = jaccard_score(jack_visited, clusters[i])
    jaccard_scores.append(js)
    print(f"Cluster {i}: {js}")

maxVal = -1
maxIdx = -1
for i in range(len(jaccard_scores)):
    if jaccard_scores[i] > maxVal:
        maxVal = jaccard_scores[i]
        maxIdx = i

print()
max_cluster = clusters[maxIdx]
print(f"Polecane strony na ktore nie wchodzil {jack_ip}")
for c in range(len(max_cluster)):
    if (max_cluster[c] == 1) and (jack_visited[c] == 0):
        print(pages[c])
print()
print(f"Wszystkie polecane strony dla {jack_ip}:")
for c in range(len(max_cluster)):
    if max_cluster[c] == 1:
        print(pages[c])