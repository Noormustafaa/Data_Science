# When You combine Multiple Series Together are known as DataFrames 

import numpy as np 
import pandas as pd 

# So now let's Create an dataFrame 
# Note we can create dataframe using list,dic, or arrays 
dic={

    'Name':['Noor','Mustafa','Rajpar'],
    'Caste': ['Rajpar','Shaikh','Ali'],
    'salary':[3,400,20]

}

df=pd.DataFrame(dic)
print(df)

# Now Let's Create a Data Frame using the list and see the difference 
data_list=[

    ['Noor',28,'Larkana',70000],
    ['Mustafa',30,'Paris',8000],
    ['Rajpar',40,'Dubai',5000]


]
df2=pd.DataFrame(data_list)
print(df2)


#         0   1        2      3
#0     Noor  28  Larkana  70000
#1  Mustafa  30    Paris   8000
#2   Rajpar  40    Dubai   5000

# it will show like this output 
# Columns name work on  default 



print(df2,"Added Columns")


# let's Create a Custom Columns

print(" New  ")

column=["Name","Age","City","Salary"]
df3=pd.DataFrame(data_list,columns=column)

print(df3)

# So we can Create using list also but we have to set columns manually 



# Selection and indexing of Columns 

#print("Here is df3 ")

# Now Let's Select the Name Column


#print(df3)

#print(df3["Name"])

#print(df3["Age"])


#print("Selecting Multiple Columns using nasted list ")

#print(df3[["Name","Age"]]) # so this is How we can Select the Multiple Columns


# Creating Or Adding the New columns in given dataset

print("Creating or adding columns")

df2['RoughAdd']=["add1","Add2","add3"]

# rEMOVE a COLUMNS...

print("How To Remove A column ")

# Let's Remove the City Column

print(df2.drop('Salary',axis=1))

print(df2)
 
