import pandas as pd

df = pd.read_csv('BIOGRID-ALL-4.4.219.mitab.txt', sep='\t')

pub_id = df['Publication Identifiers']

pub_id.to_csv('pub_id.csv', sep=',', index=False)
