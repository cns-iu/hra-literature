import pandas as pd

# Path to the uploaded CSV file
csv_file_path_uploaded = 'data/publication/hra-refs-organs.csv'

# Loading the CSV file
df_uploaded = pd.read_csv(csv_file_path_uploaded)

# Cleaning the "doi" column
df_uploaded['doi'] = (
    df_uploaded['doi']
    .str.lower()  # Convert to lowercase
    .str.strip()  # Remove leading and trailing whitespace (including spaces)
    .str.replace('https://', '')  # Remove leading "https://doi.org/" prefix
    .str.replace('doi.org/', '')  # Remove leading "doi.org/" prefix
    .str.replace('^doi ', '')  # Remove leading "doi " prefix
    .str.replace('no doi', '')  # Remove leading "doi " prefix
    .str.replace('doi:', '')  # Remove leading "https://doi.org/" prefix
    .str.rstrip('.')  # Remove trailing periods
    .str.strip()  # Remove any remaining leading and trailing whitespace
)

# Removing rows with date-like values (e.g., '2-4') in the "doi" column
date_like_pattern = r'^\d{1,2}-\d{1,2}$'
df_cleaned_final = df_uploaded[~df_uploaded['doi'].str.match(date_like_pattern, na=False)]

# Defining the path for the final cleaned CSV file
final_cleaned_csv_file_path = 'data/publication/hra-refs-cleaned.csv'

# Saving the final cleaned DataFrame to the CSV file
df_cleaned_final.to_csv(final_cleaned_csv_file_path, index=False)
