import pandas as pd
#loading titanic dataset from github

url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv"

df=pd.read_csv(url)

print(df)

#accessing head and  tail

print(df.head())

print(df.tail())

#information of the dataset

print(df.info())

print(df.columns.tolist())

#accessing a particular column

passenger_ages=df["Age"]
print(passenger_ages)
print(type(passenger_ages))

#accesig 2D dataframe

demo=df[["Name","Age","Sex"]]
print(demo.head(3))


new_df=pd.DataFrame({
    "Name":["John","Smith","Alice"],
    "Age":[28,34,29],
    "Score":[85,90,95]
})
print(new_df)

#displaying info of first row usimg iloc

print(new_df.iloc[0])

#displaying from particular position

print(new_df.iloc[0:3])

#displayimg row and column range

print(new_df.iloc[0:1,0:2])


#learning loc
print(new_df.loc[0])

copy_df=new_df.copy()

print(new_df.index)

copy_df.index=[101,102,103]
print(copy_df)

#accesing multiple columns usimg loc

df.loc[0:2,["Name","Age"]]

print(copy_df)

#changing the column name"name" to index

copy_df=copy_df.set_index("Name")
print(copy_df)

#extracting data

print(df.loc[df["Age"]<18])


#TWO Conditions check
print(df.loc[(df["Age"]<18) & (df["Sex"]=="male")])


mask = ((df["Age"] < 18) & (df["Sex"] == "male")).to_numpy()
print(mask)



#TItanic dataset https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv


#checking for missing values

print(df.isnull().sum())

#checking for duplicates

print(df.duplicated().sum())

#counting the distribution

print(df["Sex"].value_counts())

#other dropna() operations

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Ann', 'Ben', np.nan, 'Dee'],
    'age': [25, np.nan, np.nan, 40],
    'city': ['Pune', np.nan, np.nan, np.nan]
})


print(df)

print(df.dropna(how="all"))

print(df.notna().sum(axis=1))
