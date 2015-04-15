from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv('/Users/sunggyunkim/Documents/DAT6/data/titanic.csv')

# Creates Histogram of Ages
plt.hist(df.Age, bins=(range(0, 80, 1)))

# Creates a column of missing age 1 = True 0 = False
df['missing_age'] = df['Age'].isnull().astype(int)

# Display those missing age
df[df.missing_age == 1]

# Display those with age
df[df.missing_age == 0]

# Sorts the DF by name
df.sort_index(by='Name', inplace=True)

# Create a column for Married
names = df.Name

married = []
for name in names:
    name_sub = name.split(' ')
    i = 1
    for a in name_sub:
        if a == 'Mr.':
            married.append(0)
            break
        elif a == 'Miss.':
            married.append(0)
            break
        elif a == 'Master.':
            married.append(1)
            break
        elif a == 'Mrs.':
            married.append(1)
            break
        else:
            if i == len(name_sub):
                married.append(4)
                i = 0
                break
            else:
                i += 1
    i = 0

df["Married"] = married

# Shows Unclassified for Married
df[df.Married == 4]

# Create a column for Doctor
doctor = []
names = df.Name
for name in names:
    name_sub = name.split(' ')
    i = 1
    for a in name_sub:
        if a == 'Dr.':
            doctor.append(1)
            break
        else:
            if i == len(name_sub):
                doctor.append(0)
                i = 0
                break
            else:
                i += 1
    i = 0
df["Doctor"] = doctor
# Shows Doctors
df[df.Doctor == 1]

# Create a column for Rev
rev = []
names = df.Name
for name in names:
    name_sub = name.split(' ')
    i = 1
    for a in name_sub:
        if a == 'Rev.':
            rev.append(1)
            break
        else:
            if i == len(name_sub):
                rev.append(0)
                i = 0
                break
            else:
                i += 1
    i = 0
df['Rev'] = rev

# Add a coumn with only 1 Cabin Letter
cabin_letter = []
cabin_sub = ''
for cabin in df.Cabin:
    i = 0
    if type(cabin) == str:
        sub_string = cabin.split(' ')
        cabin_letter.append(cabin[0][0])
    else:
        cabin_letter.append('z')

df['Cabin_letter'] = cabin_letter

# Add Title
title = []
names = df.Name
for name in names:
    name_sub = name.split(' ')
    i = 1
    for a in name_sub:
        if a == 'Mr.':
            title.append('Mr.')
            break
        elif a == 'Miss.':
            title.append('Miss.')
            break
        elif a == 'Master.':
            title.append('Master.')
            break
        elif a == 'Mrs.':
            title.append('Mrs.')
            break
        else:
            if i == len(name_sub):
                title.append('Other')
                i = 0
                break
            else:
                i += 1
    i = 0
df['Title'] = title


