import pandas

# Creating a Dictionary
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through a dictionary:
# for (key, value) in student_dict.items():
    #Access key and value
    # print(value)
    # pass

# Converting Dictionary to DataFrame
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Looping Through a DataFrame
# Loop through columns of a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Looping Through Rows of a DataFrame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(index)
    # print(row)
    # print(row.score)
    # if row.student == "Angela":
    #     print(row.score)
    # pass

# Dictionary comprehension with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter:row.code for index, row in data.iterrows()}
print(phonetic_alphabet_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        alphabet_list = [phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        # If KeyError occurs (e.g., the user entered a number or a symbol), print an error message
        print("Sorry, only letters in the alphabet please.")
        # Call the function again to prompt the user for a valid input
        generate_phonetic()
    else:
        # If no error occurs, print the resulting phonetic code list.
        print(alphabet_list)

generate_phonetic()

