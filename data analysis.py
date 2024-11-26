import pandas as pd
import matplotlib.pyplot as plt  

data = pd.read_csv('data.csv')

print("Dataset Preview:\n", data.head())

median_age = data['Age'].median()
print(f"Median Age: {median_age}")

unique_ages = data['Age'].value_counts().count()
print(f"Total unique ages: {unique_ages}")

print("Summary Statistics:\n", data.describe(include='all'))

missing_data = data.isna().sum()
print("Missing Data by Column:\n", missing_data)

marketing_employees = data.query("Department == 'Marketing'")
print("Employees in Marketing Department:\n", marketing_employees)

lowest_salary = data['Salary'].min()
lowest_salary_emp = data[data['Salary'] == lowest_salary]
print("Employee with the lowest salary:\n", lowest_salary_emp)

department_counts = data.groupby('Department').size()
print("Employees per Department:\n", department_counts)

sorted_by_salary = data.sort_values(by='Salary', ascending=True)
print("Employees sorted by salary:\n", sorted_by_salary)

data['Seniority'] = data['Age'].map(lambda age: 'Experienced' if age >= 30 else 'Newcomer')
print("Updated Dataset with Seniority Column:\n", data)

plt.figure(figsize=(10, 6))
department_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Employees per Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
