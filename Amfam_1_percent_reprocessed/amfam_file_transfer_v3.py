import boto3
import csv
import asyncio
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Set up the S3 client
s3 = boto3.client('s3')

# Define the source and destination bucket names and paths
DIR_FROM = "cmt-rc-prod-web-b-customer"
DIR_TO = "amfam-ent-auto-ubi-cmt-reprocessed-kyd2-preprod"

files_to_transfer = []  # stores all files need to be transferred

# copy paths of missing files to a list
trip_counter = 0
size_counter = 0
with open("/home/ubuntu/cdowney/verify/files_not_in_amfam.csv") as missing_trips:
    csv_reader = csv.reader(missing_trips)
    for row in csv_reader:
        files_to_transfer.append(row[0])
        trip_counter += 1
        size_counter += float(row[-1])

print("Total number of trips need to be transferred: ", trip_counter, "total size of trips: ", size_counter)

# list to store the failed files
failed_files = []

async def copy_object(src_trip, dest_trip):
    try:
        # copying
        await loop.run_in_executor(executor, s3.copy_object, {'Bucket': DIR_TO, 'CopySource': {'Bucket': DIR_FROM, 'Key': "amfam_1_percent/trip_detail_and_summary/"+src_trip},
                       'Key': "/realtime/"+dest_trip, 'ServerSideEncryption': 'AES256', 'ACL': 'bucket-owner-full-control'})  # Assuming this will create a directory with the same path
    except Exception as e:
        print(f"Error copying {src_trip}: {e}")
        failed_files.append(src_trip)

# Use a thread pool to allow multiple I/O-bound operations to run in parallel
executor = ThreadPoolExecutor()

# Use an event loop to manage asynchronous tasks
loop = asyncio.get_event_loop()

# Loop through the missing trips list and send each of them to dest.
async def main():
    await asyncio.gather(*[copy_object(src_trip, dest_trip) for src_trip, dest_trip in tqdm(zip(files_to_transfer, files_to_transfer))])

# run the main loop
loop.run_until_complete(main())

# store failed to copy trips
with open('failed_files.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Failed Trip'])
    for trip in failed_files:
        writer.writerow([trip])
