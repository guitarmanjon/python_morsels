import csv
import sys

# Declare in and out files from command line args
in_file = sys.argv[1]
out_file = sys.argv[2]

# Base challenge - turn pipe-delimited file into a comma-delimited file
# output list
output_list = []
# read in_file
with open(in_file, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        output_list.append(str(row).replace("|", ","))

print(output_list)

# Write output file
with open(out_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in output_list:
        print(row)
        writer.writerow([row])
