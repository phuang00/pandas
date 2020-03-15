import pandas as pd

print("Hi! Welcome to Jackie and Peihua's pandas demo! Press enter to continue.")
user = input()
if user == "":
    print("Today we are going to be working with the titanic.csv file. It contains data about the passengers aboard the Titanic.")
    print("First, we are going to import the csv file.\n")
    print("Question 1: Which of the following functions is used to import a csv file in pandas?")
    print("(a) read_csv")
    print("(b) import_csv")
    print("(c) to_csv")
else:
    exit()

user = input("Your answer: ")
if user == "a":
    print("Correct!\n")
else:
    print("The correct answer was (a) read_csv!\n")

print("Here's what the data looks like after importation: \n")
print("titanic = pd.read_csv(\"titanic.csv\")\n")
titanic = pd.read_csv("titanic.csv")
print(titanic)
print()

# INFO() FUNCTION (JACKIE START HERE)
print("Question 2: Which of the following functions is used to display technical information about the data?")
print("(a) data")
print("(b) info")
print("(c) read")

user = input("Your answer: ")
if user == "b":
    print("Correct!\n")
else:
    print("The correct answer was (b) info!\n")

print("Here's what info() returns: ")
print()
print("titanic.info()\n")
print(titanic.info())
print()

# LOOKING INTO INDIVIDUAL DATAFRAMES
print("Notice the first line printed out by the info() function. It identifies our data as being stored in a DataFrame (df) object.")
print("Let's look a little closer into what these objects are.\n")
print("Below is an example of what a DataFrame object may look like: \n")

df = pd.DataFrame({"Name": ["Braund, Mr. Owen Harris",
                            "Allen, Mr. William Henry",
                            "Bonnell, Miss. Elizabeth"],
                   "Age": [22, 35, 58],
                   "Sex": ["male", "male", "female"]}
                 )
print(df)
print()
print("As you can see, a DataFrame is roughly the equivalent of a table in SQLite. There are labeled columns, with each row denoting a new entry.")
print()

# HEAD AND TAIL READING
print("Now we are going to take a look into some methods for rummaging through DataFrames.\n")
print("Question 3: Which of the following functions is used to display the first n entries of a df?")
print("(a) first")
print("(b) head")
print("(c) tail")

user = input("Your answer: ")
if user == "b":
    print("Correct!\n")
else:
    print("The correct answer was (b) head!\n")

print("To print out the first eight entries of our df, we can use the following code: \n")
print("titanic.head(8)")
print()
print(titanic.head(8))
print()

# DTYPES
print("Many different types of data can be stored in a df. We can look at what type of data is stored in each Series (column) using the dtypes attribute of a df.\n")
print("titanic.dtypes")
print()
print(titanic.dtypes)
print()
print("As you can see, some of the data stored in our titanic dataset include integers and floating points among others. ")
print()

# AGE_SEX
print("Next, we are going to examine selecting specific columns in pandas. We can do so using bracket [] notation. For example:\n")
print("age_sex = titanic[[\"Age\", \"Sex\"]]\n")
age_sex = titanic[["Age", "Sex"]]
print(age_sex)
print()

# ABOVE 35
print("Inside the brackets, we can also include conditionals. For example, if we wanted to select for ages above 35: \n")
print("above_35 = titanic[titanic[\"Age\"] > 35]")
above_35 = titanic[titanic["Age"] > 35]
print(above_35)
print()

# PCLASS 2, 3
print("Here is another example of placing conditions on our queries, using the isin() function to select for passengers in PClass 2 and 3: \n")
print("class_23 = titanic[titanic[\"Pclass\"].isin([2, 3])]")
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23)
print()

# NOT NA (JENNY START HERE)
print("pandas also makes it easy for us to isolate the missing values from our data. For instance, we can use isna() to find all the entries with a missing Cabin value: \n")
print("cabin_unknown = titanic[titanic[\"Cabin\"].isna()]")
cabin_unknown = titanic[titanic["Cabin"].isna()]
print(cabin_unknown)
print()

# USING LOC() FUNCTION
print("What ifwe only wanted to see the names of the people whose ages are unknown? We can do that using the loc() function: \n")
print("titanic.loc[titanic[\"Age\"].isna(), \"Name\"]")
print(titanic.loc[titanic['Age'].isna(), 'Name'])
print()

# SUMMARY STATISTICS USING DESCRIBE()
print("Now if we just want to focus on the ages of the people, we can use describe() to manipulate the numbers:")
print("titanic[\"Age\"].describe()")
print(titanic['Age'].describe())

# CONCAT DATA
print("To add up the values of two tables into the same column, we can use concat():")
print("s1 = pd.Series(['a', 'b'])")
s1 = pd.Series(['a', 'b'])
print(s1)
print("s2 = pd.Series(['c', 'd'])")
s2 = pd.Series(['c', 'd'])
print(s2)
print("s3 = pd.concat([s1, s2])")
s3 = pd.concat([s1, s2])
print(s3)
print()

# MERGING DATA
print("To combine the columns of two tables, we can use merge() to merge one table to the left of the other: ")
print("df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 5]})")
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 5]})
print(df1)
print("df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})")
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})
print(df2)
print("df3 = df1.merge(df2, left_on='lkey', right_on='rkey')")
df3 = df1.merge(df2, left_on='lkey', right_on='rkey')
print(df3)
