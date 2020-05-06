#!/usr/bin/python

# Forked by: angus [itsolver.net]

# Forked from:
# author : @alxndr_pereira
# github : github.com/alxpereira

# Regex from AnkitRai01 [https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/]

import sys
import csv
import re

# Make a regular expression 
# for validating an Email 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def main():
    if len(sys.argv) < 2:
        print ('Usage : ./checkem.py file.csv')
        sys.exit()
    
    filename = sys.argv[1];

    with open(filename.split('.csv')[0] + '_export.csv', 'w') as csvfile:
        fieldnames = ['email', 'valid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open(sys.argv[1], "r") as f:
        # with open(filename, "r") as f:
            reader = csv.reader(f, delimiter="\t")

            for i, line in enumerate(reader):
                email = line[0]
                
                # pass the regualar expression 
            	# and the string in search() method 
                if(re.search(regex,email)): 
                    is_valid = True
                else: 
                    is_valid = False 

                writer.writerow({'email': email, 'valid': str(is_valid)})
                print (email + ' => ' + str(is_valid))

if __name__ == "__main__":
    main()