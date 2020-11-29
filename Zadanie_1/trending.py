import pandas as pd

INPUT_FILE = 'data_full.csv'
threshold = 0.5  # %
data = pd.read_csv(INPUT_FILE, usecols=['address'])


most_popular_sites = data['address'].value_counts(ascending=False)
most_popular_sites.to_csv('most_popular_sites.csv', index=True, header=['number_of_occurences'])

percent_of_occurrences = (most_popular_sites / data.size) * 100
percent_of_occurrences = percent_of_occurrences[percent_of_occurrences > threshold]

percent_of_occurrences.to_csv('percent_of_occurrences.csv', index=True, header=['percent_of_occurrences'])
