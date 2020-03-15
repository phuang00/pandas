import pandas as pd
df = pd.DataFrame({"Name": ["Braund, Mr. Owen Harris",
                            "Allen, Mr. William Henry",
                            "Bonnell, Miss. Elizabeth"],
                   "Age": [22, 35, 58],
                   "Sex": ["male", "male", "female"]}
                 )
print(df)
print()
print(df["Age"])

ages = pd.Series([22, 35, 58], name="Age")
print()
print(ages)
print(ages.max())
print(df.describe())

titanic = pd.read_csv("titanic.csv")
print(titanic)
print(titanic.head(6))
print(titanic.tail(7))
print(titanic.dtypes)
# have to install openpyxl module first
titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)
# have to install xlrd module first
titanic = pd.read_excel('titanic.xlsx', sheet_name='passengers')
print(titanic.info())
age_sex = titanic[["Age", "Sex"]]
print(age_sex)
print(age_sex.shape)
above_35 = titanic[titanic["Age"] > 35]
print(above_35)
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23)
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na)
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)
