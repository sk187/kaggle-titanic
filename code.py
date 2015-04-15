import pandas as pd
import numpy as np
import matplotlib.pylab as plt


df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Titanic/train.csv')
df.info()

# Dropping unnesseary columns
cols = ['Ticket', 'Cabin', 'Name']
df = df.drop(cols, axis=1)

# Interpolate missing ages values with a median
df['Age'] = df['Age'].interpolate()

# Creating numerical representations of Pclass, Sex, and Embarked
dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
    dummies.append(pd.get_dummies(df[col]))
    titanic_dummies = pd.concat(dummies, axis=1)

df = pd.concat((df, titanic_dummies), axis=1)
df = df.drop(['Pclass', 'Sex', 'Embarked'], axis=1)

# Interpolate missing ages values with a median
df['Age'] = df['Age'].interpolate()

# Removes NaN Values
df = df.dropna()

X = df.values
y = df['Survived'].values

X = np.delete(X,1,axis=1)

#Exploration of Data
d.groupby('Parch').Survived.mean()
d.groupby('SibSp').Survived.mean()
d.groupby('Age').Survived.mean()
d.groupby('Pclass').Survived.mean()
d.groupby('Sex').Survived.mean()

d.groupby(['Sex', 'Pclass']).Survived.mean()


from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)

from sklearn import tree

clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

from sklearn import ensemble
clf = ensemble.RandomForestClassifier(n_estimators=100)
clf.fit (X_train, y_train)
clf.score (X_test, y_test)

clf = ensemble.GradientBoostingClassifier()
clf.fit (X_train, y_train)
clf.score (X_test, y_test)
