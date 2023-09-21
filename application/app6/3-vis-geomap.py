import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the author data from CSV
author_geo_df = pd.read_csv('data/results/app6/author-geo-ct.csv')

# Load the GeoJSON file containing country shapes
countries_gdf = gpd.read_file('data/vis/countries.geojson')

# Merge the GeoDataFrame with the author data on country code
merged_gdf = countries_gdf.merge(author_geo_df, left_on="ISO_A2", right_on="country_code", how="left")

# Fill NaN values with 0 for countries without author data
merged_gdf['count'].fillna(0, inplace=True)

# Plotting the data using the 'OrRd' colormap
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_gdf.plot(column='count', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='#36AE90', legend=True)
ax.set_title('Number of Authors by Country')
plt.show()

# Save the figure
fig_path_svg = "data/results/app6/authors_by_country_map.svg"
fig.savefig(fig_path_svg, bbox_inches="tight", format="svg")
