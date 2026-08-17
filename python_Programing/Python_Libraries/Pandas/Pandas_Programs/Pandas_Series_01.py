# Pandas Series ! 

# A Series is a one-dimensional labeled array capable of holding any data type . The axis labels are Collecltivly
# called the index. 
# A series is a one dimensional array it means [1,2,4,5] like this . and capable of holding any datatype means
# we can store in series int , char , or string means in array we can store muliple data type in series but not combine .

# the Axis labels means it's indexes .

# Note: Series always in vertical and arrays are always in horizontal 

# So Let's create the Series 

import numpy as np 
import pandas as pd 

# So before Creating a Series first creates a labels 

labels=['a','b','c']

my_list=[10,20,30]

# now let's create an numpy array 

arr=np.array([10,20,30])

# now Creating the Dictionary 

d= {"Noor":10,"rajpar":30,"Mustafa":30}

# Now Let's Create an Series 

Ser=pd.Series(my_list)# It will ask on which data you want to create an series 
print(Ser) # it will give answer with labels by default.

# Now Let's Create Custom labels 
CustomL=pd.Series(my_list,index=labels) # and our labels are a,b,c
print(CustomL)

# Now Creating labels with arrays 

arSeries=pd.Series(arr)
print(arSeries)

# Custom labels with arrays 

# And if you will send dictionary then it means we are sending Created labels to them ! 

Diction=pd.Series(d)
print(Diction)

# So this was all about Series  and Collection of Series are are known as Dataframe 