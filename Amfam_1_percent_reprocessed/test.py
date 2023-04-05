import csv


# Open the CSV file for reading
def count_files(filename):
    with open(filename, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Initialize a row count variable
        row_count = 0
        # Iterate through each row in the CSV file
        for row in reader:
            # Increment the row count for each row
            row_count += 1

        # Print the total number of rows
        print(f'Total number of rows: {row_count}')
        return row_count


am_fam = count_files('prefix_stripped_combined.csv')

cmt = count_files('prefix_stripped_file_info.csv')


print( "the difference count in files: ", cmt - am_fam)

#checking which files are
