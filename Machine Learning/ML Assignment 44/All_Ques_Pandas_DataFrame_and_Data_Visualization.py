# Assignment 44 — Pandas DataFrame and Data Visualization

############################################################
# Q1: Create a DataFrame for student marks and print basic
# information like shape, columns, and data types.
############################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("Q1: Basic DataFrame Information")
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data Types:\n", df.dtypes)


############################################################
# Q2: Use the DataFrame from Q1 and print descriptive
# statistics using .describe().
############################################################

print("\nQ2: Descriptive Statistics")
print(df.describe())


############################################################
# Q3: Add a new column 'Total' to the DataFrame as the sum
# of all subject marks.
############################################################

df['Total'] = df['Math'] + df['Science'] + df['English']

print("\nQ3: DataFrame with Total Marks")
print(df)


############################################################
# Q4: Display students who scored more than 85 in Science.
############################################################

print("\nQ4: Students Scoring More Than 85 in Science")
print(df[df['Science'] > 85])


############################################################
# Q5: Replace 'Charlie' with 'Chris' in the 'Name' column.
############################################################

df['Name'] = df['Name'].replace('Charlie', 'Chris')

print("\nQ5: DataFrame After Replacing Name")
print(df)


############################################################
# Q6: Sort the DataFrame by 'Total' marks in descending order.
############################################################

df_sorted = df.sort_values(by='Total', ascending=False)

print("\nQ6: DataFrame Sorted by Total Marks")
print(df_sorted)


############################################################
# Q7: Create a bar plot of student names vs total marks.
############################################################

plt.figure(figsize=(8, 5))

plt.bar(df['Name'], df['Total'])
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Total Marks by Student')

plt.tight_layout()
plt.show()


############################################################
# Q8: Plot a line chart of marks for 'Alice' across all
# subjects.
############################################################

alice_data = df[df['Name'] == 'Alice']

if not alice_data.empty:
    alice_marks = alice_data[
        ['Math', 'Science', 'English']
    ].values.flatten()

    subjects = ['Math', 'Science', 'English']

    plt.figure(figsize=(8, 5))

    plt.plot(subjects, alice_marks, marker='o')
    plt.title("Alice's Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
else:
    print("\nQ8: Alice is not present in the DataFrame.")
    print("Available students:", df['Name'].tolist())


############################################################
# Q9: Create a DataFrame with missing values and fill them
# with the corresponding column mean.
############################################################

data2 = {
    'Name': ['Dan', 'Eve', 'Frank'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df2 = pd.DataFrame(data2)

df2.fillna(
    df2.mean(numeric_only=True),
    inplace=True
)

print("\nQ9: DataFrame After Filling Missing Values")
print(df2)


############################################################
# Q10: Drop the 'English' column from the original DataFrame.
############################################################

df_dropped = df.drop(columns=['English'])

print("\nQ10: DataFrame After Dropping English Column")
print(df_dropped)


