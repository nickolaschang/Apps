import os

import pandas as pd

csv_files_list = []


def list_all_csv():
	filename = os.listdir(os.getcwd())
	for file in filename:
		if file.endswith('.csv'):
			csv_files_list.append(file)
	for csv_file in csv_files_list:
		print("File Found:", csv_file)
	return csv_files_list


list_all_csv()
selected_csv = input("Select CSV file: \n").lower() + '.csv'
if selected_csv in csv_files_list:
	with open(selected_csv, 'r,w') as csv_file:
		pass

