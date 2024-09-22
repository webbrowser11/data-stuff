import csv

# so far we have learned how to sort a list.
random_numbers = [1, 4, 3, 2]
sorted_numbers = sorted(random_numbers)
print(sorted_numbers)

# and... sort a CSV file
# replace name with your actual windows username.
with open('C:/Users/graham/Downloads/data-example.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    ages = []
    
    # now lest collect all the ages
    for row in reader:
        ages.append(int(row['age']))

# next we find the avrage age
average_age = sum(ages) / len(ages)
print(f"The average age is: {average_age}")