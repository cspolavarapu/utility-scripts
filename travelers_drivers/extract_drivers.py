import csv
import os
from tqdm import tqdm

path = '/Users/cspolavarapu/Downloads/travelers_drivers/'
files = os.listdir(path)
count = 0

drivers_set = set()
trip_list = list()
# count total number of csv files in the directory
for file in files:
    if os.path.isfile(file) and file.endswith('.csv'):
        with open(file, 'r') as temp_file:
            reader = csv.reader(temp_file)
            next(reader)

            for row in tqdm(reader):
                trip_list.append(row[1])
                if row[0] not in drivers_set:
                    drivers_set.add(row[0])
    print('Processing ' +file+ " finished.... !!!")

print("Total unique drivers: ", len(drivers_set))
print("Total number of trips: ", len(trip_list))

# Write the trip_list to a CSV file
with open('trip_list.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["TRIP LIST"])
    for trip in trip_list:
        writer.writerow([trip])

print('Trip list saved to trip_list.csv file.')






