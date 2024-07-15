# make a folder, put this file in that folder and open that folder with VS code (make that folder as directory).
import csv

# Example data to be written to the CSV file from a list of list
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 22, 'Chicago']
]

# Specify the file name
csv_file_path = 'example.csv'

# Writing data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(data[0])
    
    # Write the remaining rows
    writer.writerows(data[1:])

print(f'Data has been written to {csv_file_path}')

