# Abdullah AlShammari, aa62899@usc.edu
# Description:

# PYTHON MODULES
# import user-installed modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pandas row options, set to display 100 rows
pd.set_option('display.max_rows', 100)

# Read CSV file
happiness_income_log = pd.read_csv('happyscore_income.csv')

# View Columns & Null Counts For All Dataframe Columns
# print(happiness_income_log.columns)
# print(happiness_income_log.info())

# Shape of DataFrame
# print("Happiness Income Log Shape:")
# print(happiness_income_log.shape)

# Clean Data Frame
# print("Shape before dropping duplicates and unneeded columns: ")
# print(happiness_income_log.shape)

# Drop Duplicates
happiness_income_log = happiness_income_log.drop_duplicates()
# Drop Nulls
happiness_income_log = happiness_income_log.dropna()

# Shape after Dropping Null & Duplicates
print("Shape after dropping duplicates and unneeded columns: ")
print(happiness_income_log.shape)

# Create new Dataframe with only GDP and happyScore
df = happiness_income_log[['GDP', 'happyScore']]
df.head()


# Finding Correlation between GDP and happyScore using different methods

# Method == pearson
print(df.corr(method ='pearson'))

# Method == kendall
print(df.corr(method='kendall'))

# Method == spearman
print(df.corr(method='spearman'))

# Finding Correlation between income_inequality and std_satisfaction (using the pearson method)

# Choose columns income_inequality and std_satisfaction
df2 = happiness_income_log[['income_inequality', 'std_satisfaction']]

# Drop Duplicates & Nulls
df2 = df2.drop_duplicates()
df2 = df2.dropna()

# Find correlation
print(df2.corr(method ='pearson'))

