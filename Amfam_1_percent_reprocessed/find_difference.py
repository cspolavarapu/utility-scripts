import csv
import json


def write_to_csv(difference, input_file, output_file_name):
    # storing the difference to csv file
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        count = 0
        for file in [input_file]:
            with open(file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] in difference:  # checking if the row of input file in the difference
                        writer.writerow(row)
                        count += 1
        return count


# First file
with open('prefix_stripped_CMT_file_info.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    next(reader1)
    cmt_files_set = set(row[0] for row in reader1)  # creating a set with the name of the file: 0th column in CSV
    print(f"Total # of rows in {file1.name}: ", len(cmt_files_set))

# second file
with open('prefix_stripped_combined_AMFAM_final.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    next(reader2)
    amfam_files_set = set(row[0] for row in reader2)  # creating a set with the name of the file: 0th column in CSV
    print(f"Total # of rows in {file2.name}: ", len(amfam_files_set))

print("Difference between both in total [Before matching file names] : ", len(cmt_files_set) - len(amfam_files_set))

print("\n Comparing File Names in both sets.......")
# Find the values that are in column 1 of one file but not the other
unique_values = cmt_files_set.difference(amfam_files_set)

diff_1 = write_to_csv(unique_values, 'prefix_stripped_CMT_file_info.csv', 'files_not_in_amfam.csv')
print(" # of Files in CMT bucket but not in AmFam : ", diff_1)

unique_values2 = amfam_files_set.difference(cmt_files_set)
diff_2 = write_to_csv(unique_values2, 'prefix_stripped_combined_AMFAM_final.csv', 'files_not_in_cmt.csv')
print(" # of Files in AmFam but not in CMT : ", diff_2)

# create a Json file with missing trips from the CSV file created earlier

filename = 'files_not_in_amfam.csv'

with open(filename, 'r') as missing_trips:
    reader = csv.reader(missing_trips)
    result_dict = {}
    for row in reader:
        row_data = row[0].split('/')
        if result_dict.get(row_data[0]) is None:
            result_dict[row_data[0]] = [row_data[-1]]
        else:
            result_dict[row_data[0]].append(row_data[-1])

    missing_trips = json.dumps(result_dict, indent=4)

    print("\n \n Creating a JSON file with missing driver IDs and Trip files....")

    with open("missing_files.json", "w") as output_file:
        output_file.write(missing_trips)
    print(f"    \n Saving Complete ! Look for {output_file.name}")
