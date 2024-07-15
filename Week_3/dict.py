# make a folder, put this file in that folder and open that folder with VS code (make that folder as directory).
import csv

fieldnames = ['Name', 'Age', 'City']
with open('dict.csv',mode= 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'Name': 'Alice', 'Age': 25, 'City': 'New York'})
