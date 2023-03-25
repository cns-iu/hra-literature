#extract the Publication Identifier
import pandas as pd

df = pd.read_csv('INTERACTION-GENE_HUMAN.csv', skiprows=14)
reference_df = pd.DataFrame(columns=['Reference', 'Type'])
reference_df['Reference'] = df['Publication Identifier(s)']
reference_df['Type'] = 'genetic interaction'
reference_df.to_csv('output3.csv', index=False)
