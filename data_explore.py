# Avg Price of Ticket by Class
df.groupby('Pclass').Fare.mean()
# 1         84.154687
# 2         20.662183
# 3         13.675550

# Avg Age by Class (with missing ages)
df.groupby('Pclass').Age.mean()
# 1         38.233441
# 2         29.877630
# 3         25.140620

# Avg Price of Ticket by Embarked
df.groupby('Embarked').Fare.mean()
# C           59.954144
# Q           13.276030
# S           27.079812

# Avg Class by Cabin Letter
df.groupby('Cabin_letter').Pclass.mean()
# Cabin_letter
# A               1.000000
# B               1.000000
# C               1.000000
# D               1.121212
# E               1.312500
# F               2.384615
# G               3.000000
# T               1.000000
# z               2.639010

# Avg Fare by Cabin Letter
df.groupby('Cabin_letter').Fare.mean()
# Cabin_letter
# A                39.623887
# B               113.505764
# C               100.151341
# D                57.244576
# E                46.026694
# F                18.696792
# G                13.581250
# T                35.500000
# z                19.157325

# Avg Price of Ticket for Class by Port
df.groupby(['Embarked', 'Pclass']).Fare.mean()
# Embarked  Pclass
# C         1         104.718529
#           2          25.358335
#           3          11.214083
# Q         1          90.000000
#           2          12.350000
#           3          11.183393
# S         1          70.364862
#           2          20.327439
#           3          14.644083

# Count of Port 
df.groupby('Embarked').Embarked.count()
# Embarked
# C           168
# Q            77
# S           644

# Avg Age by Title
df.groupby('Title').Age.mean() 
# Title
# Master.     4.574167
# Miss.      21.773973
# Mr.        32.368090
# Mrs.       35.898148
# Other      42.384615

# Avg Survival Rate by Sex and Cabin 
df.groupby(['Cabin_letter','Sex']).Survived.mean()
# Cabin_letter  Sex   
# A             female    1.000000
#               male      0.428571
# B             female    1.000000
#               male      0.400000
# C             female    0.888889
#               male      0.343750
# D             female    1.000000
#               male      0.466667
# E             female    0.933333
#               male      0.588235
# F             female    1.000000
#               male      0.375000
# G             female    0.500000
# T             male      0.000000
# z             female    0.654378
#               male      0.136170

# Avg Survival by Embarked Port
df.groupby('Embarked').Survived.mean()
# Embarked
# C           0.553571
# Q           0.389610
# S           0.336957

df.groupby(['Embarked','Pclass','Sex']).Survived.mean()
Embarked  Pclass  Sex   
# C         1       female    0.976744
#                   male      0.404762
#           2       female    1.000000
#                   male      0.200000
#           3       female    0.652174
#                   male      0.232558
# Q         1       female    1.000000
#                   male      0.000000
#           2       female    1.000000
#                   male      0.000000
#           3       female    0.727273
#                   male      0.076923
# S         1       female    0.958333
#                   male      0.354430
#           2       female    0.910448
#                   male      0.154639
#           3       female    0.375000
#                   male      0.128302

df.groupby('Title').Survived.mean()
# Title
# Master.    0.575000
# Miss.      0.697802
# Mr.        0.156673
# Mrs.       0.792000
# Other      0.444444

df.groupby(['Embarked', 'Pclass', 'Title']).Age.count()
# Embarked  Pclass  Title 
# C         1       Miss.       20
#                   Mr.         32
#                   Mrs.        14
#                   Other        8
#           2       Master.      1
#                   Miss.        3
#                   Mr.          7
#                   Mrs.         4
#           3       Master.      2
#                   Miss.       12
#                   Mr.         23
#                   Mrs.         4
# Q         1       Miss.        1
#                   Other        1
#           2       Miss.        1
#                   Other        1
#           3       Master.      4
#                   Miss.        8
#                   Mr.         10
#                   Mrs.         2
# S         1       Master.      3
#                   Miss.       23
#                   Mr.         55
#                   Mrs.        19
#                   Other        8
#           2       Master.      8
#                   Miss.       28
#                   Mr.         75
#                   Mrs.        37
#                   Other        8
#           3       Master.     18
#                   Miss.       49
#                   Mr.        196
#                   Mrs.        27

df.groupby(['Embarked', 'Pclass', 'Title']).Age.mean()
# Embarked  Pclass  Title
# C         1       Miss.      33.500000
#                   Mr.        39.593750
#                   Mrs.       41.428571
#                   Other      37.125000
#           2       Master.     1.000000
#                   Miss.      15.666667
#                   Mr.        29.500000
#                   Mrs.       21.750000
#           3       Master.     6.210000
#                   Miss.       9.333333
#                   Mr.        26.652174
#                   Mrs.       28.250000
# Q         1       Miss.      33.000000
#                   Other      44.000000
#           2       Miss.      30.000000
#                   Other      57.000000
#           3       Master.     5.250000
#                   Miss.      19.687500
#                   Mr.        37.300000
#                   Mrs.       35.500000
# S         1       Master.     5.306667
#                   Miss.      26.478261
#                   Mr.        42.736364
#                   Mrs.       39.368421
#                   Other      49.625000
#           2       Master.     2.416250
#                   Miss.      22.839286
#                   Mr.        33.073333
#                   Mrs.       34.972973
#                   Other      38.375000
#           3       Master.     5.277778
#                   Miss.      17.204082
#                   Mr.        28.530612
#                   Mrs.       34.148148