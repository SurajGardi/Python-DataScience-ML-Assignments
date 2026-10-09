############################################################
# Assignment 45 — Pandas Data Preprocessing and Visualization
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

############################################################
# Q1: Normalize the 'Math' scores using Min-Max scaling.
############################################################

df['Math_Norm'] = (
    (df['Math'] - df['Math'].min()) /
    (df['Math'].max() - df['Math'].min())
)

print("\nQ1: Normalized Math Scores")
print(df[['Name', 'Math', 'Math_Norm']])


############################################################
# Q2: Create a gender column and perform one-hot encoding.
############################################################

df['Gender'] = ['F', 'M', 'M']

df_encoded = pd.get_dummies(df, columns=['Gender'])

print("\nQ2: DataFrame After One-Hot Encoding")
print(df_encoded)


############################################################
# Q3: Group students by gender and calculate average marks.
############################################################

print("\nQ3: Average Marks Grouped by Gender")

print(
    df.groupby('Gender')[['Math', 'Science', 'English']].mean()
)


############################################################
# Q4: Plot a pie chart of subject marks for 'Bob'.
############################################################

bob_data = df[df['Name'] == 'Bob']

if not bob_data.empty:
    bob = bob_data[
        ['Math', 'Science', 'English']
    ].values.flatten()

    labels = ['Math', 'Science', 'English']

    plt.figure(figsize=(7, 7))

    plt.pie(
        bob,
        labels=labels,
        autopct='%1.1f%%'
    )

    plt.title("Bob's Subject Wise Distribution")
    plt.tight_layout()
    plt.show()

else:
    print("\nQ4: Bob is not present in the DataFrame.")
    print("Available students:", df['Name'].tolist())


############################################################
# Q5: Add a 'Status' column based on total marks.
# Students with Total >= 250 pass; otherwise, they fail.
############################################################

# Calculate total marks before assigning the status.
df['Total'] = df['Math'] + df['Science'] + df['English']

df['Status'] = df['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'
)

print("\nQ5: Student Pass/Fail Status")
print(df[['Name', 'Total', 'Status']])


############################################################
# Q6: Count how many students passed.
############################################################

print("\nQ6: Total Number of Students Passed")

print("Total Passed:", df[df['Status'] == 'Pass'].shape[0])


############################################################
# Q7: Export the final DataFrame to a CSV file.
############################################################

df.to_csv("students_result.csv", index=False)

print("\nQ7: DataFrame exported to students_result.csv")


############################################################
# Q8: Plot a histogram of Math marks.
############################################################

plt.figure(figsize=(8, 5))

plt.hist(df['Math'], bins=5, edgecolor='black')
plt.title("Distribution of Math Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()


############################################################
# Q9: Rename the 'Math' column to 'Mathematics'.
############################################################

df.rename(
    columns={'Math': 'Mathematics'},
    inplace=True
)

print("\nQ9: DataFrame After Renaming Math Column")
print(df.head())


############################################################
# Q10: Plot a boxplot for English marks to check distribution
# and identify potential outliers.
############################################################

plt.figure(figsize=(7, 5))

plt.boxplot(df['English'])
plt.title("Boxplot of English Marks")
plt.ylabel("Marks")
plt.grid(True)

plt.tight_layout()
plt.show()
