import pandas as pd

df = pd.read_csv('mitab.txt', sep='\t')

pub_id = df['Publication Identifiers']

pub_id.to_csv('pub_id.csv', index=False)
