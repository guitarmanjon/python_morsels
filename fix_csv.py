import csv
import sys

# Declare in and out files from command line args
in_file = sys.argv[1]
out_file = sys.argv[2]

# Base challenge - turn pipe-delimited file into a comma-delimited file

# read in_file
with open(in_file, 'rt') as open_file:
    reader = csv.reader(open_file)
    
    # Write output file
    with open(out_file, 'w', newline='') as write_file:
        writer = csv.writer(write_file, delimiter=',')
        for row in reader:
            writer.writerow(row)
