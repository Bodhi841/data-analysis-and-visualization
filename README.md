# data-analysis-and-visualization
This repository contains a Python script for performing data analysis and visualization using the pandas and matplotlib libraries. The script demonstrates various operations on a dataset, making it a practical example of how to manipulate, analyze, and visualize data in Python.

Code Highlights:
Data Loading:

The script reads a CSV file (data.csv) into a pandas DataFrame for analysis.
It assumes the dataset contains columns like Age, Department, and Salary.
Data Exploration:

Head of the Data: Displays the first few rows for a quick overview of the dataset structure.
Descriptive Statistics: Generates summary statistics (mean, median, min, max, etc.) for numerical columns using describe().
Data Analysis:

Average and Unique Value Calculations:
Computes the average age and counts unique values in the Age column.
Missing Values:
Identifies missing values in each column using isnull().sum().
Filtering Data:
Filters rows based on specific conditions (e.g., employees in the Engineering department).
Min/Max Values:
Finds the employee(s) with the highest salary.
Data Transformation:

Adds a new column, Experience, categorized as Senior or Junior based on the age.
Data Aggregation:

Counts the frequency of values in a specific column (e.g., employees in each department).
Sorting:

Sorts the dataset based on the Age column in descending order.
Data Visualization:

Uses matplotlib to create visual representations:
Pie chart displaying the proportion of employees in each department.
