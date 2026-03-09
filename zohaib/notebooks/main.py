
import os
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("raw_data.csv")

# Copy of original data frame before cleaning.
df_before = df.copy()

# provide Concise summary of dataframe.
# print(df.info())

#provide statistical summary of dataframe.
# print(df.describe())

# check duplicates
# print(df['CustomerID'].duplicated().sum())


#check missing values in the dataframe.
# print(df.isnull().sum())

df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Gender'] = df['Gender'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')
df['AccountType'] = df['AccountType'].fillna('Unavailable')
df['Balance'] = df['Balance'].fillna(0)
df['LoanStatus'] = df['LoanStatus'].fillna('Missing')
df['Email'] = df['Email'].fillna('Not provided')


#remove duplicates based on customer id
df.drop_duplicates(subset='CustomerID', inplace=True)


#convert data format
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

#convert data type of age and Balance from float to int
df['Age']=df['Age'].astype(int)
df['Balance']=df['Balance'].astype(int)

# Clean data by removing extra spaces and standarize text.
df['Name'] = df['Name'].str.title().str.strip()
df['City'] = df['City'].str.title().str.strip()
df['AccountType'] = df['AccountType'].str.title().str.strip()
df['LoanStatus'] = df['LoanStatus'].str.title().str.strip()
df['Gender'] = (
    df['Gender']
    .str.strip()
    .str.lower()
    .replace({'m':'male','f':'female'})
    .str.title()
)

#add coloumn currency with balance.
df['Balance_PKR'] = df['Balance'].apply(lambda x: f"{x} Rs")
#add coloumn Gender code with gender
df['Gender_Code'] = df['Gender'].astype('category').cat.codes

df['Email'] = df['Email'].str.replace('_', '', regex=False)

# Category for gender coloumn.

# print(df['Gender'].unique())

#outlier detection and removal using IQR method for balance coloumn.

Q1 = df["Balance"].quantile(0.25)
Q3 = df["Balance"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df["Balance"] >= lower) & (df["Balance"] <= upper)]


# Removing outliers check
# print(df.shape)




# Compare basic metrics
comparison = pd.DataFrame({
    "Metric": ["Rows", "Columns", "Missing Values", "Duplicates (CustomerID)"],
    "Before": [
        df_before.shape[0],
        df_before.shape[1],
        df_before.isnull().sum().sum(),
        df_before.duplicated(subset='CustomerID').sum()  # check duplicates by CustomerID
    ],
    "After": [
        df_clean.shape[0],
        df_clean.shape[1],
        df_clean.isnull().sum().sum(),
        df_clean.duplicated(subset='CustomerID').sum()
    ]
})
print("===== Before vs After Cleaning Summary =====")
print(comparison)


# Visual comparison.
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
sns.boxplot(x=df_before["Balance"])
plt.title("Before Cleaning")

plt.subplot(1,2,2)
sns.boxplot(x=df_clean["Balance"])
plt.title("After Cleaning")

plt.show()

print(df.head(10))



file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cleaned_data.csv")
df.to_csv(file_path, index=False)
