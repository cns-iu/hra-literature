#!/bin/bash

# Download the Excel file
curl -O http://117.50.127.228/CellMarker/CellMarker_download_files/file/Cell_marker_Human.xlsx

# Use Python with pandas to convert Excel to CSV
python3 -c "
import pandas as pd
data = pd.read_excel('Cell_marker_Human.xlsx')
data.to_csv('human_cell_markers.csv', index=False)
"

echo "Conversion completed. The CSV file is saved as human_cell_markers.csv."
