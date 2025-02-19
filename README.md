# NATO Phonetic Alphabet Converter

This Python program converts user-inputted words into their corresponding phonetic code using the NATO Phonetic Alphabet. It first reads a CSV file to create a dictionary where each letter is mapped to its phonetic equivalent (e.g., "A" → "Alfa", "B" → "Bravo"). The program then prompts the user to enter a word, converts it to uppercase, and generates a list of phonetic words. If the input contains non-alphabet characters (such as numbers or symbols), the user is prompted to enter a valid word again.

Additionally, the project demonstrates how to:

Create a dictionary in Python.
Loop through a dictionary using .items().
Convert a dictionary into a Pandas DataFrame.
Iterate through rows of a DataFrame using .iterrows().
Use dictionary comprehension to create a new dictionary from a DataFrame.