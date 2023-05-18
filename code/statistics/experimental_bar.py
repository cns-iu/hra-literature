import os
import csv

root_folder = 'tissue-bar-graphs-a46dbf29d2f611720a93e62d562e9fa9511e3072\\csv'
output_file = 'output.csv'

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Folder B Name', 'File C Name', 'File Size'])

    for folder_b in os.listdir(root_folder):
        folder_b_path = os.path.join(root_folder, folder_b)
        if os.path.isdir(folder_b_path):
            for file_c in os.listdir(folder_b_path):
                file_c_path = os.path.join(folder_b_path, file_c)
                if os.path.isfile(file_c_path):
                    file_size = os.path.getsize(file_c_path)
                    writer.writerow([folder_b, file_c, file_size])

print(f"CSV output saved to {output_file}.")
