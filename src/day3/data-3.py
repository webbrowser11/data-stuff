# now we know how to do sorting lets use a csv file

import csv

# lets read the CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    ages = []
    
    # now lest collect all the ages
    for row in reader:
        ages.append(int(row['age']))

# next we find the avrage age
average_age = sum(ages) / len(ages)
print(f"The average age is: {average_age}")
