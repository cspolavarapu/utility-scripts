# #import csv
#
# # Open the input CSV file for reading
# with open('file_info.csv', 'r') as input_file:
#     # Open the output CSV file for writing
#     with open('prefix_stripped_CMT_file_info.csv', 'w', newline='') as output_file:
#         reader = csv.reader(input_file)
#         writer = csv.writer(output_file)
#         # Iterate through each row in the input file
#         for row in reader:
#             # Remove the prefix from the first column of the row
#             row[0] = row[0].lstrip('amfam_1_percent/trip_detail_and_summary/')
#             # Write the updated row to the output file
#             writer.writerow(row)
#         print("operation completed")
#

import csv

prefix = "amfam_1_percent/trip_detail_and_summary/"  # Replace with the actual prefix to be removed
filename = "file_info.csv"  # Replace with the actual filename of the CSV file

# Open the CSV file for reading and create a new CSV file for writing
with open(filename, 'r') as input_file, open('prefix_stripped_CMT_file_info.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header row to the new CSV file
    writer.writerow(next(reader))

    # Iterate over the remaining rows and remove the prefix from the first column
    for row in reader:
        row[0] = row[0].replace(prefix, "")
        writer.writerow(row)
    print("Operation completed")
