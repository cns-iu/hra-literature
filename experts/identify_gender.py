import pandas as pd
import gender_guesser.detector as gender

# Initialize gender detector
d = gender.Detector()

# Load the data
data = pd.read_excel("path_to_file")

# Add a gender column
data['gender'] = data['firstName'].apply(lambda x: d.get_gender(x))

# Print the first few rows
data.to_csv('output.csv')
