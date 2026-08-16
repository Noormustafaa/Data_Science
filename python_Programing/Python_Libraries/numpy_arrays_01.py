import numpy as np 

# Basic Arrary Creation
#Note : You must know that Whenever You are Creating an numpy array it is creating Using List 
# Example 
arr=np.array([1,2,3,4,5]) # So inside the Array bractes we have Created the List 
print(arr)

print(type(arr))

a=[1,3,5.5,"Noor"] # Hence this Is The List 
print(a)

# So If We Want To Convert This List To Array then it will show the Error ! 
# Because Array can store just same data type 

arr2=np.array(a)
print(arr2) # Note : So when we convert it  array in output python will convert all data types into the Strings
print(type[arr2]) # it will give output dtype<'U32' means it has been convert into the Strings 

# Note If You will Remove String data type then there is an float number so it will convert all value into the 
# Float

# Note : Array And list has another thing that is one thing is known as Vectors And Another thing is known as 
# Matrics 


#Vectors are Somthing which are Created in One Dimensional 
# Example : you have create a list [1,2,3,4,5] So this is One Dimensional 

# Matrics have multiple rows and multips columns 

# So For Creating Matrics what you have to do is Create a list and inside it another list create  [[1,2,3],[4,5,6,8],[8,9,10]]

# Note : List Does not Support the Multi-Dimensional 
l=[[1,2,3],[4,5,6],[7,8,9]]  
print(l,"Iam List") # in output it is look like a one dimensional 

# So If we convert same thing into the array you will be able to see as a output in multi-dimensional

lis=np.array(l)
print(lis) # so it is give now output in multi-Dimensional 

# And There Are some Other Things as well like 3 dimensions 4 dimensional and all of these things are 
# Called Tensors , Like Tensor flow Library we already heard this.
# Note Above then 2 dimensions are known as Tensors 