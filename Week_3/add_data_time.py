# make a folder, put this file in that folder and open that folder with VS code (make that folder as directory).
import csv
from datetime import datetime

    # mode parameter:
    #     It specifies the mode in which the file is opened. The most common modes include:
    #         'r': Read (default mode). Opens the file for reading.
    #         'w': Write. Opens the file for writing. If the file already exists, it will be truncated (emptied). If the file doesn't exist, a new file will be created.
    #         'a': Append. Opens the file for writing, but appends new data to the end of the file instead of truncating it.
    #         'b': Binary mode. Appends 'b' to the mode, such as 'rb' or 'wb', to indicate binary mode.
    #         '+': Read and Write. Opens the file for both reading and writing.

    # newline parameter:
    #     It controls how newline characters are handled.
    #     When reading, if newline is None (default), universal newline mode is enabled, and all common newline characters ('\r', '\n', '\r\n') are recognized.
    #     When writing, newline controls what character sequences are used to represent newlines in the file. Use newline='' to specify that no conversion should be done.

def create_csv_file(file_path, header):
    
    # Create a new CSV file with the specified header
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    print(f'CSV file "{file_path}" created with header: {header}')

def add_data_to_csv(file_path, data):
    # Get the current timestamp and format it as a string
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Combine timestamp with the provided data
    data_with_timestamp = [timestamp] + data
    
    # Append the combined data to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_with_timestamp)
    print(f'Data added to CSV file "{file_path}": {data_with_timestamp}')
    

def read_csv_file(file_path):
    # Read and print the data from the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Specify file path and header
csv_file_path = 'example_with_timestamp.csv'
csv_header = ['Timestamp', 'Name', 'Age', 'City']

# Create CSV file with header
create_csv_file(csv_file_path, csv_header)

# Add data to the CSV file with timestamp
data_to_add = ['Alice', 25, 'New York']
add_data_to_csv(csv_file_path, data_to_add)

data_to_add = ['Bob', 30, 'San Francisco']
add_data_to_csv(csv_file_path, data_to_add)


# Read and print data from the CSV file
print('\nReading data from CSV file:')
read_csv_file(csv_file_path)
