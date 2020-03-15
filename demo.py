import pandas as pd

print("Hi! Welcome to Jackie and Jenny's pandas demo! Press enter to continue.")
user = input()
if user == "":
    print("Today we are going to be working with the titanic.csv file. It contains data about the passengers aboard the Titanic.")
    print("First, we are going to import the csv file into a DataFrame, which is the pandas equivalent of a SQLite table.\n")
    print("Question 1: Which of the following commands is used to import a csv file?")
    print("(a) read_csv")
    print("(b) import_csv")
    print("(c) to_csv")
else:
    exit()

user = input("Your answer: ")
if user == "a":
    print("Correct!")
else:
    print("The correct answer was (a) read_csv!")

print("Here's what the data looks like after importation: \n")
titanic = pd.read_csv("titanic.csv")
print(titanic)
print()

print("Each")
# INFO() FUNCTION

# LOOKING INTO INDIVIDUAL DATAFRAMES

# HEAD AND TAIL READING

# DTYPES

# AGE_SEX

# ABOVE 35

# PCLASS 2, 3

# NOT NA

# USING LOC() FUNCTION

# SUMMARY STATISTICS USING DESCRIBE()

# MERGING / CONCAT DATA
