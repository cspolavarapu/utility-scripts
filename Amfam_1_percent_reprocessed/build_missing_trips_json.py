import csv
import json

# Open csv file for reading and creating a json with driver IDs and missing trips
filename = 'files_not_in_amfam.csv'

with open(filename, 'r') as missing_trips:
    reader = csv.reader(missing_trips)
    result_dict = {}
    next(reader)
    for row in reader:
        row_data = row[0].split('/')
        if result_dict.get(row_data[0]) is None:
            result_dict[row_data[0]] = [row_data[-1]]
        else:
            result_dict[row_data[0]].append(row_data[-1])

    missing_trips = json.dumps(result_dict, indent=4)

    print("Creating a JSON file with missing driver IDs and Trip files....")

    with open("missing_files.json", "w") as output_file:
        output_file.write(missing_trips)
    print(f"Saving Complete ! Look for {output_file.name}")



