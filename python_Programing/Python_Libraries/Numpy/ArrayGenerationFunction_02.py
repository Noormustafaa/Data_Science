# Now We Will Learn how To Generate The Arrays 

#1 range Function 
import numpy as np

arRange=np.arange(1,11)

print(arRange) # so it will generate on array from 1 to 10 

# Note : We can Generate Some Zeros 
#zeros=np.zeros(6)
#print(zeros)

# We can also generate the multi-dimensions

#zeros1=np.zeros((4,8)) # for That just use double brackets 
#print(zeros1)

ones1= np.ones(6)
print(ones1)

# For Multi-Dimensions

ones2=np.ones((4,8))
print(ones2)



# Now Linespace...

# Linear Space we can also say this 

arr3=np.linspace(1,5,3) # so in between 1 and 5 we want 3 numbers

print(arr3)

arr4=np.linspace(1,5,10)
print(arr4) # so it will generate 10 numbers in between the 1 and 5 

# So this was the usecase of linspace  Called Linear space 
