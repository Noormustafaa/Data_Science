# Note : Random Library Allows us to generate some Randome numbers 
# And numpy creates us to Generate some arrays 
# So What if Numpy and arrays work together? 
# Array will be Created with some random numbers 
# So when we install numpy library then random library also install automatically 
# 
#  
import numpy as np

Rand=np.random.rand(5)
print(Rand) # so it will generate a random numbers 5 
# ANd Note  that all the values will come in between 0 and 1 and this 
# is the concept of Normalization in statistics 

# And in Standardization we get values in between 3 and -3 

# So what if we want values in between that .

# so write
stand=np.random.randn(10)
print(stand) # so this will give output as a between 3 and -3

# Now Genetating Integer Numbers 

Integ1=np.random.randint(6)
print(Integ1)

# in array ?

r=np.random.randint(10,20,10)
print(r)
