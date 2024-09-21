# lets make a simple grading Bot for the teachers out there.
# make sure to replace "name" with your real name

import pandas as pd

# Lets load the CSV file
data = pd.read_csv('C:/Users/name/Downloads/data.csv')

# Now lets calculate the score.
average_score = data['score'].mean()
print(f"Average score: {average_score}")

# now lets make the function to assign letter grades
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'f'

# Now lets applt the grading function to the score column
data['grade'] = data['score'].apply(assign_grade)

# finally Display the updated data with grades
print(data)