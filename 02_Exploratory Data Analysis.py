import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option('display.max_columns', None)

# Plot style
sns.set_style('whitegrid')

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')
#load dataset

df1 = pd.read_csv('04_Clean Data 1.csv')

df2 = pd.read_csv('05_Clean Data 2.csv')


df1.info()
df2.info()

#Statistical Summary
df1.describe(include='all')
df2.describe(include='all')

numerical_columns = df1.select_dtypes(include=['int64','float64']).columns

#BOXPLOT 1
for col in numerical_columns:

    plt.figure(figsize=(8,4))

    sns.boxplot(x=df1[col])

    plt.title(col)

    plt.show()
    
#CORRELATION MATRIX 2
corr = df1[numerical_columns].corr()

plt.figure(figsize=(10,8))

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.show()

#COMPANY WISE JOBS 3
df1['company_name'].value_counts().head(10)
plt.figure(figsize=(12,6))
df1['company_name'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")
plt.show()

#TOP JOB TITLES 4
plt.figure(figsize=(12,6))
df1['title'].value_counts().head(10).plot(kind='bar')
plt.title("Top Job Titles")
plt.show()

#TOP LOCATIONS  5
plt.figure(figsize=(12,6))
df1['location'].value_counts().head(10).plot(kind='bar')
plt.title("Top Hiring Locations")
plt.show()

#WORK DISTRIBUTION 6
plt.figure(figsize=(8,6))
sns.countplot(data=df1,
              x='formatted_work_type')
plt.xticks(rotation=45)
plt.show()

#SALARY DISTRIBUTION 7
plt.figure(figsize=(10,6))
sns.histplot(df1['avg_salary'],
             bins=30,
             kde=True)

plt.title("Average Salary Distribution")
plt.show()

# APPLICATION DISTRIBUTION 8
plt.figure(figsize=(10,6))
sns.histplot(df1['applies'],
             bins=30,
             kde=True)
plt.title("Applications Distribution")
plt.show()

#AVERAGE SALARY BY WORK TYPE 9
salary_work = df1.groupby('formatted_work_type')['avg_salary'].mean()
plt.figure(figsize=(8,6))
salary_work.plot(kind='bar')
plt.ylabel("Average Salary")
plt.show()

#TOP PAYING COMPANIES 10
top_salary = df1.groupby('company_name')['avg_salary'].mean()
top_salary = top_salary.sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
top_salary.plot(kind='bar')
plt.title("Top Paying Companies")
plt.show()

#VIEWS VS APPLICATION 11
plt.figure(figsize=(10,6))
sns.scatterplot(data=df1,
                x='views',
                y='applies')
plt.title("Views vs Applications")
plt.show()

#TOP HIRING COMPANY FOR DATA JOBS 12
plt.figure(figsize=(12,5))
df2['company'].value_counts().head(10).plot(kind='bar', color='green')
plt.title("Top Data Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Job Count")
plt.xticks(rotation=45)
plt.show()

#TOP LOCATIONS FOR DATA JOBS 13
plt.figure(figsize=(12,5))
df2['location'].value_counts().head(5).plot(kind='bar', color='green')
plt.title("Top  Data Hiring Locations")
plt.xlabel("Location")
plt.ylabel("Job Count")
plt.xticks(rotation=45)
plt.show()

#DESCRIPTION LENGTH
df2['Description Length'] = df2['description'].str.len()

#DISTRIBUTION OF DESCRIPTION LENGTH 14
plt.figure(figsize=(10,5))
sns.histplot(df2['Description Length'], bins=20, kde=True)
plt.title("Distribution of Job Description Length")
plt.show()

#LONGEST JOB DESCRIPTION
df2[['title','company','Description Length']]\
.sort_values(by='Description Length', ascending=False)\
.head(10)

#WORD COUNT
df2['Word Count'] = df2['description'].apply(lambda x: len(str(x).split()))

#CORRELATION 15
corr = df2[['Description Length','Word Count']].corr()
plt.figure(figsize=(5,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

#Most Common Words (Basic NLP)
from collections import Counter
text = " ".join(df2['description'].dropna())
words = text.lower().split()
common_words = Counter(words).most_common(20)
common_words

