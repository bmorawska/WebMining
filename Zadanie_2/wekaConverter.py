import pandas as pd

filename = 'clear_ready_logs.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

titles = []
idxText = []
for iter, line in enumerate(lines):
    if 'Page' in line:
        title = lines[iter - 1]
        titles.append(title[:-1])
        idxStart = iter + 1
        idxText.append(idxStart)

texts = []
for i in range(len(idxText) - 1):
    text = lines[idxText[i]: (idxText[i + 1] - 2)]
    text = ' '.join([str(elem) for elem in text])
    text = text.replace('\n', ' ')
    texts.append(str(text))

lastText = lines[idxText[-1]:]
lastText = ' '.join([str(elem) for elem in lastText])
lastText = lastText.replace('\n', ' ')
texts.append(str(lastText))

df = pd.DataFrame(titles, columns=['title'])
df['text'] = texts
df.to_csv('ftims_logs.csv', index=False, columns=['title', 'text'])

"""
Zamienić w notatniku "" na spacje i ' na spację.
"""
