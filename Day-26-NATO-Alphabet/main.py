import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Loop through rows of a dataframe WITHOUT dict comprehension
# nato_dict = {}
# for (index, row) in nato_df.iterrows():
#     nato_dict[row.letter] = row.code

# Loop through rows of a dataframe WITH dict comprehension
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

# # Without list comprehension
# result = []
# for letter in user_word:
#     if letter in nato_dict.keys():
#         result.append(nato_dict[letter])

# With list comprehension
result = [nato_dict[letter] for letter in user_word]

print(result)
