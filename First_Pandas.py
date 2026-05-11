import pandas as pd

data = pd.read_csv(r'C:\Users\Joey\OneDrive\Desktop\grades.csv')

average_grades = data.groupby('Student Name')['Grade'].mean()

max_grade = data['Grade'].max()
print('Highest grade in the class: ', max_grade)

min_grade = data['Grade'].min()
print('Lowest grade in the class: ', min_grade)

class_average = data['Grade'].mean()
print('Average grade of the class: ', class_average)

data['Pass/Fail'] = data['Grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
print(data)

pass_count = data[data['Pass/Fail'] == 'Pass'].shape[0]
fail_count = data[data['Pass/Fail'] == 'Fail'].shape[0]
print("Number of students passed:", pass_count)
print("Number of students failed:", fail_count)
