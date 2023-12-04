import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pycountry

# read data
file_path = 'data/validation/author-geo-ct.csv' 
data = pd.read_csv(file_path, header=None, names=['Country Code', 'Count'])

# change to ISO3 format
def convert_to_iso3(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).alpha_3
    except:
        return None

data['iso_a3'] = data['Country Code'].apply(convert_to_iso3)

data['Count'] = pd.to_numeric(data['Count'], errors='coerce') 
data.dropna(subset=['Count'], inplace=True) 

# load world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world_data = world.merge(data, on='iso_a3', how='left')
world_data['Count'] = world_data['Count'].fillna(0)

# exclude Antarctica
world_data_no_antarctica = world_data[world_data['name'] != 'Antarctica']

norm = mcolors.SymLogNorm(linthresh=1000, linscale=1, base=10, vmin=0, vmax=world_data_no_antarctica['Count'].max())

# visualize map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world_data_no_antarctica.plot(column='Count', ax=ax, legend=True, 
                              norm=norm, cmap='Reds', edgecolor='grey', linewidth=0.5,
                              legend_kwds={'label': "Count by Country", 'orientation': "horizontal"})
ax.set_title('World Map Visualization of Counts by Country (Red Color Scheme, With Grey Borders, Without Antarctica)', fontsize=14)
ax.set_axis_off()
plt.show()
