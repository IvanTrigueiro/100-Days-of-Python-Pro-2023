import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Loop through rows of a data frame
for (index, rows) in student_df.iterrows():
    print(rows)
    print(rows.score)
