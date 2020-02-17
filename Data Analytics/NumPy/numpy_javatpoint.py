

#  https://www.javatpoint.com/numpy-ndarray

import numpy


a = numpy.array  


print(a)


numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)


# 1 	object 	It represents the collection object. It can be a list, tuple, dictionary, set, etc.
# 2 	dtype 	We can change the data type of the array elements by changing this option to the specified type. The default is none.
# 3 	copy 	It is optional. By default, it is true which means the object is copied.
# 4 	order 	There can be 3 possible values assigned to this option. It can be C (column order), R (row order), or A (any)
# 5 	subok 	The returned array will be base class array by default. We can change this to make the subclasses passes through by setting this option to true.
# 6 	ndmin 	It represents the minimum dimensions of the resultant array.



a = numpy.array([1, 2, 3])  

print(a)

print(type(a))


a = numpy.array([[1, 2, 3], [4, 5, 6]])  

print(a)


a = numpy.array([1, 3, 5, 7], complex) 

print(a)




import numpy as np

arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])  

print(arr.ndim)

print(arr)


#finding the size of each item in the array  
import numpy as np  
a = np.array([[1,2,3]])  
print("Each item contains",a.itemsize,"bytes")  


#finding the data type of each array item  
import numpy as np  
a = np.array([[1,2,3]])  
print("Each item is of the type",a.dtype)  



import numpy as np  
a = np.array([[1,2,3,4,5,6,7]])  
print("Array Size:",a.size)  
print("Shape:",a.shape)  











# Finding the size of each array element

# The itemsize function is used to get the size of each array item. It returns the number of bytes taken by each array element.

# Consider the following example.
# Example

#     #finding the size of each item in the array  

import numpy as np  
a = np.array([[1,2,3]])  
print("Each item contains",a.itemsize,"bytes")  

# Output:

# Each item contains 8 bytes.













# Finding the data type of each array item

# To check the data type of each array item, the dtype function is used. Consider the following example to check the data type of the array items.
# Example

#     #finding the data type of each array item  

import numpy as np  
a = np.array([[1,2,3]])  
print("Each item is of the type",a.dtype)  

# Output:

# Each item is of the type int64













# Finding the shape and size of the array

# To get the shape and size of the array, the size and shape function associated with the numpy array is used.

# Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2,3,4,5,6,7]])  
print("Array Size:",a.size)  
print("Shape:",a.shape)  

# Output:

# Array Size: 7
# Shape: (1, 7)





























# Reshaping the array objects

# By the shape of the array, we mean the number of rows and columns of a multi-dimensional array. However, the numpy module provides us the way to reshape the array by changing the number of rows and columns of the multi-dimensional array.

# The reshape() function associated with the ndarray object is used to reshape the array. It accepts the two parameters indicating the row and columns of the new shape of the array. 




# Example

import numpy as np  
a = np.array([[1,2],[3,4],[5,6]])  
print("printing the original array..")  
print(a)  
a=a.reshape(2,3)  
print("printing the reshaped array..")  
print(a)  

# Output:

# printing the original array..
# [[1 2]
#  [3 4]
#  [5 6]]
# printing the reshaped array..
# [[1 2 3]
#  [4 5 6]]





















# Slicing in the Array

# Slicing in the NumPy array is the way to extract a range of elements from an array. Slicing in the array is performed in the same way as it is performed in the python list.

# Consider the following example to print a particular element of the array.
# Example

import numpy as np  
a = np.array([[1,2],[3,4],[5,6]])  
print(a[0,1])  
print(a[2,0])  

# Output:

# 2
# 5

# The above program prints the 2nd element from the 0th index and 0th element from the 2nd index of the array. 






# Linspace

# The linspace() function returns the evenly spaced values over the given interval. The following example returns the 10 evenly separated values over the given interval 5-15
# Example

import numpy as np  
a=np.linspace(5,15,10) #prints 10 values which are evenly spaced over the given interval 5-15  
print(a)  

# Output:

# [ 5.          6.11111111  7.22222222  8.33333333  9.44444444 10.55555556
#  11.66666667 12.77777778 13.88888889 15.        ]









# Finding the maximum, minimum, and sum of the array elements

# The NumPy provides the max(), min(), and sum() functions which are used to find the maximum, minimum, and sum of the array elements respectively.

# Consider the following example.
# Example

import numpy as np  
a = np.array([1,2,3,10,15,4])  
print("The array:",a)  
print("The maximum element:",a.max())  
print("The minimum element:",a.min())  
print("The sum of the elements:",a.sum())  

# Output:

# The array: [ 1  2  3 10 15  4]
# The maximum element: 15
# The minimum element: 1
# The sum of the elements: 35









# NumPy Array Axis

# A NumPy multi-dimensional array is represented by the axis where axis-0 represents the columns and axis-1 represents the rows. We can mention the axis to perform row-level or column-level calculations like the addition of row or column elements.

# To calculate the maximum element among each column, the minimum element among each row, and the addition of all the row elements, consider the following example.
# Example

import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
print("The array:",a)  
print("The maximum elements of columns:",a.max(axis = 0))   
print("The minimum element of rows",a.min(axis = 1))    # a.min(axis = 1)
print("The sum of all rows",a.sum(axis = 1))  

# Output:

# The array: [[1  2  30]
# 		   [10  15  4]]
# The maximum elements of columns: [10 15 30]
# The minimum element of rows [1 4]
# The sum of all rows [33 29]












# Finding square root and standard deviation

# The sqrt() and std() functions associated with the numpy array are used to find the square root and standard deviation of the array elements respectively.

# Standard deviation means how much each element of the array varies from the mean value of the numpy array.

# Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
print(np.sqrt(a))  
print(np.std(a))  

# Output:

# [[1.         1.41421356 5.47722558]
#  [3.16227766 3.87298335 2.        ]]
# 10.044346115546242

















# Arithmetic operations on the array

# The numpy module allows us to perform the arithmetic operations on multi-dimensional arrays directly.

# In the following example, the arithmetic operations are performed on the two multi-dimensional arrays a and b.
# Example

import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])  
print("Sum of array a and b\n",a+b)  
print("Product of array a and b\n",a*b)  
print("Division of array a and b\n",a/b)  








# Array Concatenation

# The numpy provides us with the vertical stacking and horizontal stacking which allows us to concatenate two multi-dimensional arrays vertically or horizontally.

# Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])  
print("Arrays vertically concatenated\n",np.vstack((a,b)));  
print("Arrays horizontally concatenated\n",np.hstack((a,b)))  

# Output:

# Arrays vertically concatenated
#  [[ 1  2 30]
#  [10 15  4]
#  [ 1  2  3]
#  [12 19 29]]
# Arrays horizontally concatenated
#  [[ 1  2 30  1  2  3]
#  [10 15  4 12 19 29]]







# NumPy Datatypes

# The NumPy provides a higher range of numeric data types than that provided by the Python. A list of numeric data types is given in the following table.
# SN 	Data type 	Description
# 1 	bool_ 	It represents the boolean value indicating true or false. It is stored as a byte.
# 2 	int_ 	It is the default type of integer. It is identical to long type in C that contains 64 bit or 32-bit integer.
# 3 	intc 	It is similar to the C integer (c int) as it represents 32 or 64-bit int.
# 4 	intp 	It represents the integers which are used for indexing.
# 5 	int8 	It is the 8-bit integer identical to a byte. The range of the value is -128 to 127.
# 6 	int16 	It is the 2-byte (16-bit) integer. The range is -32768 to 32767.
# 7 	int32 	It is the 4-byte (32-bit) integer. The range is -2147483648 to 2147483647.
# 8 	int64 	It is the 8-byte (64-bit) integer. The range is -9223372036854775808 to 9223372036854775807.
# 9 	uint8 	It is the 1-byte (8-bit) unsigned integer.
# 10 	uint16 	It is the 2-byte (16-bit) unsigned integer.
# 11 	uint32 	It is the 4-byte (32-bit) unsigned integer.
# 12 	uint64 	It is the 8 bytes (64-bit) unsigned integer.
# 13 	float_ 	It is identical to float64.
# 14 	float16 	It is the half-precision float. 5 bits are reserved for the exponent. 10 bits are reserved for mantissa, and 1 bit is reserved for the sign.
# 15 	float32 	It is a single precision float. 8 bits are reserved for the exponent, 23 bits are reserved for mantissa, and 1 bit is reserved for the sign.
# 16 	float64 	It is the double precision float. 11 bits are reserved for the exponent, 52 bits are reserved for mantissa, 1 bit is used for the sign.
# 17 	complex_ 	It is identical to complex128.
# 18 	complex64 	It is used to represent the complex number where real and imaginary part shares 32 bits each.
# 19 	complex128 	It is used to represent the complex number where real and imaginary part shares 64 bits each. 






# NumPy dtype

# All the items of a numpy array are data type objects also known as numpy dtypes. A data type object implements the fixed size of memory corresponding to an array.

# We can create a dtype object by using the following syntax. 








#     numpy.dtype(object, align, copy)  

# The constructor accepts the following object.

# Object: It represents the object which is to be converted to the data type.

# Align: It can be set to any boolean value. If true, then it adds extra padding to make it equivalent to a C struct.

# Copy: It creates another copy of the dtype object.
# Example 1

import numpy as np  
d = np.dtype(np.int32)  
print(d)  

# Output:

# int32


























# Creating a Structured data type

# We can create a map-like (dictionary) data type which contains the mapping between the values. For example, it can contain the mapping between employees and salaries or the students and the age, etc.

# Consider the following example.
# Example 1

import numpy as np  
d = np.dtype([('salary',np.float)])  
print(d)  


# Example 2

import numpy as np  
d=np.dtype([('salary',np.float)])  
arr = np.array([(10000.12,),(20000.50,)],dtype=d)  
print(arr['salary'])  




































# Numpy Array Creation

# The ndarray object can be constructed by using the following routines. 

# Numpy.empty

# As the name specifies, The empty routine is used to create an uninitialized array of specified shape and data type.

# The syntax is given below. 





#     numpy.empty(shape, dtype = float, order = 'C')  

# It accepts the following parameters.

#     Shape: The desired shape of the specified array.
#     dtype: The data type of the array items. The default is the float.
#     Order: The default order is the c-style row-major order. It can be set to F for FORTRAN-style column-major order.

# Example

import numpy as np  
arr = np.empty((3,2), dtype = int)  
print(arr)  








# NumPy.Zeros

# This routine is used to create the numpy array with the specified shape where each numpy array item is initialized to 0.

# The syntax is given below.

#     numpy.zeros(shape, dtype = float, order = 'C')  

# It accepts the following parameters.

#     Shape: The desired shape of the specified array.
#     dtype: The data type of the array items. The default is the float.
#     Order: The default order is the c-style row-major order. It can be set to F for FORTRAN-style column-major order.

# Example

import numpy as np  
arr = np.zeros((3,2), dtype = int)  
print(arr)  










# NumPy.ones

# This routine is used to create the numpy array with the specified shape where each numpy array item is initialized to 1.

# The syntax to use this module is given below.

#     numpy.ones(shape, dtype = none, order = 'C')  

# It accepts the following parameters.

#     Shape: The desired shape of the specified array.
#     dtype: The data type of the array items.
#     Order: The default order is the c-style row-major order. It can be set to F for FORTRAN-style column-major order.

# Example

import numpy as np  
arr = np.ones((3,2), dtype = int)  
print(arr)  
























# Numpy array from existing data

# NumPy provides us the way to create an array by using the existing data.
# numpy.asarray

# This routine is used to create an array by using the existing data in the form of lists, or tuples. This routine is useful in the scenario where we need to convert a python sequence into the numpy array object.

# The syntax to use the asarray() routine is given below.




#     numpy.asarray(sequence,  dtype = None, order = None)  

# It accepts the following parameters.

#     sequence: It is the python sequence which is to be converted into the python array.
#     dtype: It is the data type of each item of the array.
#     order: It can be set to C or F. The default is C.

# Example: creating numpy array using the list

import numpy as np  
l=[1,2,3,4,5,6,7]  
a = np.asarray(l);  
print(type(a))  
print(a)  




# Example: creating a numpy array using Tuple

import numpy as np  
l=(1,2,3,4,5,6,7)     
a = np.asarray(l);  
print(type(a))  
print(a)  




# Example: creating a numpy array using more than one list

import numpy as np  
l=[[1,2,3,4,5,6,7],[8,9]]  
a = np.asarray(l);  
print(type(a))  
print(a)  











# numpy.frombuffer

# This function is used to create an array by using the specified buffer. The syntax to use this buffer is given below.

#     numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)  

# It accepts the following parameters.

#     buffer: It represents an object that exposes a buffer interface.
#     dtype: It represents the data type of the returned data type array. The default value is 0.
#     count: It represents the length of the returned ndarray. The default value is -1.
#     offset: It represents the starting position to read from. The default value is 0.






# Example

import numpy as np  
l = b'hello world'  
print(type(l))  
a = np.frombuffer(l, dtype = "S1")  
print(a)  
print(type(a))  
























# numpy.fromiter

# This routine is used to create a ndarray by using an iterable object. It returns a one-dimensional ndarray object.

# The syntax is given below.

#     numpy.fromiter(iterable, dtype, count = - 1)  

# It accepts the following parameters.

#     Iterable: It represents an iterable object.
#     dtype: It represents the data type of the resultant array items.
#     count: It represents the number of items to read from the buffer in the array.

# Example

import numpy as np  
list = [0,2,4,6]  
it = iter(list)  
x = np.fromiter(it, dtype = float)  
print(x)  
print(type(x))  














# Numpy Arrays within the numerical range

# This section of the tutorial illustrates how the numpy arrays can be created using some given specified range.
# Numpy.arrange

# It creates an array by using the evenly spaced values over the given interval. The syntax to use the function is given below.

#     numpy.arrange(start, stop, step, dtype)  

# It accepts the following parameters. 




    # start: The starting of an interval. The default is 0.
    # stop: represents the value at which the interval ends excluding this value.
    # step: The number by which the interval values change.
    # dtype: the data type of the numpy array items.





# Example

import numpy as np  
arr = np.arange(0,10,2,float)  
print(arr)  



# Example

import numpy as np  
arr = np.arange(10,100,5,int)  
print("The array over the given range is ",arr)  










# NumPy.linspace

# It is similar to the arrange function. However, it doesn?t allow us to specify the step size in the syntax.

# Instead of that, it only returns evenly separated values over a specified period. The system implicitly calculates the step size.

# The syntax is given below.

#     numpy.linspace(start, stop, num, endpoint, retstep, dtype)   

# It accepts the following parameters.

#     start: It represents the starting value of the interval.
#     stop: It represents the stopping value of the interval.
#     num: The amount of evenly spaced samples over the interval to be generated. The default is 50.
#     endpoint: Its true value indicates that the stopping value is included in the interval.
#     rettstep: This has to be a boolean value. Represents the steps and samples between the consecutive numbers.
#     dtype: It represents the data type of the array items.



# Example

import numpy as np  
arr = np.linspace(10, 20, 5)  
print("The array over the given range is ",arr)  



# Example

import numpy as np  
arr = np.linspace(10, 20, 5, endpoint = False)  
print("The array over the given range is ",arr)  






# numpy.logspace

# It creates an array by using the numbers that are evenly separated on a log scale.

# The syntax is given below.

#     numpy.logspace(start, stop, num, endpoint, base, dtype)  

# It accepts the following parameters.

#     start: It represents the starting value of the interval in the base.
#     stop: It represents the stopping value of the interval in the base.
#     num: The number of values between the range.
#     endpoint: It is a boolean type value. It makes the value represented by stop as the last value of the interval.
#     base: It represents the base of the log space.
#     dtype: It represents the data type of the array items.





# Example

import numpy as np  
arr = np.logspace(10, 20, num = 5, endpoint = True)  
print("The array over the given range is ",arr)  



# ExAMPLE

import numpy as np  
arr = np.logspace(10, 20, num = 5,base = 2, endpoint = True)  
print("The array over the given range is ",arr)  















# NumPy Broadcasting

# In Mathematical operations, we may need to consider the arrays of different shapes. NumPy can perform such operations where the array of different shapes are involved.

# For example, if we consider the matrix multiplication operation, if the shape of the two matrices is the same then this operation will be easily performed. However, we may also need to operate if the shape is not similar.

# Consider the following example to multiply two arrays.




# Example

import numpy as np  
a = np.array([1,2,3,4,5,6,7])  
b = np.array([2,4,6,8,10,12,14])  
c = a*b;  
print(c)  





# However, in the above example, if we consider arrays of different shapes, we will get the errors as shown below.
# Example

import numpy as np  
a = np.array([1,2,3,4,5,6,7])  
b = np.array([2,4,6,8,10,12,14,19])  
c = a*b;  
print(c)  




# In the above example, we can see that the shapes of the two arrays are not similar and therefore they cannot be multiplied together. NumPy can perform such operation by using the concept of broadcasting.

# In broadcasting, the smaller array is broadcast to the larger array to make their shapes compatible with each other.
# Broadcasting Rules

# Broadcasting is possible if the following cases are satisfied.

#     The smaller dimension array can be appended with '1' in its shape.
#     Size of each output dimension is the maximum of the input sizes in the dimension.
#     An input can be used in the calculation if its size in a particular dimension matches the output size or its value is exactly 1.
#     If the input size is 1, then the first data entry is used for the calculation along the dimension.

# Broadcasting can be applied to the arrays if the following rules are satisfied.

#     All the input arrays have the same shape.
#     Arrays have the same number of dimensions, and the length of each dimension is either a common length or 1.
#     Array with the fewer dimension can be appended with '1' in its shape.

# Let's see an example of broadcasting.
# Example



import numpy as np  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
b = np.array([2,4,6,8])  
print("\nprinting array a..")  
print(a)  
print("\nprinting array b..")  
print(b)  
print("\nAdding arrays a and b ..")  
c = a + b;  
print(c)  











# NumPy Array Iteration

# NumPy provides an iterator object, i.e., nditer which can be used to iterate over the given array using python standard Iterator interface.

# Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
print("Printing array:")  
print(a);  
print("Iterating over the array:")  
for x in np.nditer(a):  
    print(x,end=' ')  









# Order of the iteration doesn't follow any special ordering like row-major or column-order. However, it is intended to match the memory layout of the array.

# Let's iterate over the transpose of the array given in the above example.
# Example

import numpy as np  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
print("Printing the array:")  
print(a)  
print("Printing the transpose of the array:")  
at = a.T  
print(at)  
  
#this will be same as previous   
for x in np.nditer(at):  
    print(print("Iterating over the array:"))  
for x in np.nditer(a):  
    print(x,end=' ')  










# Order of Iteration

# As we know, there are two ways of storing values into the numpy arrays:

#     F-style order
#     C-style order

# Let's see an example of how the numpy Iterator treats the specific orders (F or C).
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
  
print("\nPrinting the array:\n")  
  
print(a)  
  
print("\nPrinting the transpose of the array:\n")  
at = a.T  
  
print(at)  
  
print("\nIterating over the transposed array\n")  
  
for x in np.nditer(at):  
    print(x, end= ' ')  
  
print("\nSorting the transposed array in C-style:\n")  
  
c = at.copy(order = 'C')  
  
print(c)  
  
print("\nIterating over the C-style array:\n")  
for x in np.nditer(c):  
    print(x,end=' ')  
      
  
d = at.copy(order = 'F')  
  
print(d)  
print("Iterating over the F-style array:\n")  
for x in np.nditer(d):  
    print(x,end=' ')  







# We can mention the order 'C' or 'F' while defining the Iterator object itself. Consider the following example.
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
  
print("\nPrinting the array:\n")  
  
print(a)  
  
print("\nPrinting the transpose of the array:\n")  
at = a.T  
  
print(at)  
  
print("\nIterating over the transposed array\n")  
  
for x in np.nditer(at):  
    print(x, end= ' ')  
  
print("\nSorting the transposed array in C-style:\n")  
  
print("\nIterating over the C-style array:\n")  
for x in np.nditer(at, order = 'C'):  
    print(x,end=' ')


















# Array Values Modification

# We can not modify the array elements during the iteration since the op-flag associated with the Iterator object is set to readonly.

# However, we can set this flag to readwrite or write only to modify the array values. Consider the following example.
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
  
print("\nPrinting the original array:\n")  
  
print(a)  
  
print("\nIterating over the modified array\n")  
  
for x in np.nditer(a, op_flags = ['readwrite']):  
    x[...] = 3 * x;  
    print(x,end = ' ')  































# NumPy Bitwise Operators

# Numpy provides the following bitwise operators.
# SN 	Operator 	Description
# 1 	bitwise_and 	It is used to calculate the bitwise and operation between the corresponding array elements.
# 2 	bitwise_or 	It is used to calculate the bitwise or operation between the corresponding array elements.
# 3 	invert 	It is used to calculate the bitwise not the operation of the array elements.
# 4 	left_shift 	It is used to shift the bits of the binary representation of the elements to the left.
# 5 	right_shift 	It is used to shift the bits of the binary representation of the elements to the right.
# bitwise_and Operation

# The NumPy provides the bitwise_and() function which is used to calculate the bitwise_and operation of the two operands.

# The bitwise and operation is performed on the corresponding bits of the binary representation of the operands. If both the corresponding bit in the operands is set to 1, then only the resultant bit in the AND result will be set to 1 otherwise it will be set to 0.






# Example

import numpy as np  
  
a = 10  
b = 12  
  
print("binary representation of a:",bin(a))  
print("binary representation of b:",bin(b))  
print("Bitwise-and of a and b: ",np.bitwise_and(a,b))  






# AND Truth Table

# The output of the AND result of the two bits is 1 if and only if both the bits are 1 otherwise it will be 0.
# A 	B 	AND (A, B)
# 0 	0 	0
# 0 	1 	0
# 1 	0 	0
# 1 	1 	1
# bitwise_or Operator

# The NumPy provides the bitwise_or() function which is used to calculate the bitwise or operation of the two operands.

# The bitwise or operation is performed on the corresponding bits of the binary representation of the operands. If one of the corresponding bit in the operands is set to 1 then the resultant bit in the OR result will be set to 1; otherwise it will be set to 0.
# Example

import numpy as np  
  
a = 50  
b = 90  
print("binary representation of a:",bin(a))  
print("binary representation of b:",bin(b))  
print("Bitwise-or of a and b: ",np.bitwise_or(a,b))  









# Or truth table

# The output of the OR result of the two bits is 1 if one of the bits are 1 otherwise it will be 0.
# A 	B 	Or (A, B)
# 0 	0 	0
# 0 	1 	1
# 1 	0 	1
# 1 	1 	1
# Invert operation

# It is used to calculate the bitwise not the operation of the given operand. The 2's complement is returned if the signed integer is passed in the function.

# Consider the following example.
# Example

import numpy as np  
  
arr = np.array([20],dtype = np.uint8)  
print("Binary representation:",np.binary_repr(20,8))  
  
print(np.invert(arr))  
  
print("Binary representation: ", np.binary_repr(235,8))  





# It shifts the bits in the binary representation of the operand to the left by the specified position. An equal number of 0s are appended from the right. Consider the following example.
# Example

import numpy as np  
  
print("left shift of 20 by 3 bits",np.left_shift(20, 3))  
  
print("Binary representation of 20 in 8 bits",np.binary_repr(20, 8))  
  
print("Binary representation of 160 in 8 bits",np.binary_repr(160,8))  












# Right Shift Operation

# It shifts the bits in the binary representation of the operand to the right by the specified position. An equal number of 0s are appended from the left. Consider the following example.
# Example

import numpy as np  
  
print("left shift of 20 by 3 bits",np.right_shift(20, 3))  
  
print("Binary representation of 20 in 8 bits",np.binary_repr(20, 8))  
  
print("Binary representation of 160 in 8 bits",np.binary_repr(160,8))  

















# NumPy String Functions

# NumPy contains the following functions for the operations on the arrays of dtype string.
# SN 	Function 	Description
# 1 	add() 	It is used to concatenate the corresponding array elements (strings).
# 2 	multiply() 	It returns the multiple copies of the specified string, i.e., if a string 'hello' is multiplied by 3 then, a string 'hello hello' is returned.
# 3 	center() 	It returns the copy of the string where the original string is centered with the left and right padding filled with the specified number of fill characters.
# 4 	capitalize() 	It returns a copy of the original string in which the first letter of the original string is converted to the Upper Case.
# 5 	title() 	It returns the title cased version of the string, i.e., the first letter of each word of the string is converted into the upper case.
# 6 	lower() 	It returns a copy of the string in which all the letters are converted into the lower case.
# 7 	upper() 	It returns a copy of the string in which all the letters are converted into the upper case.
# 9 	split() 	It returns a list of words in the string.
# 9 	splitlines() 	It returns the list of lines in the string, breaking at line boundaries.
# 10 	strip() 	Returns a copy of the string with the leading and trailing white spaces removed.
# 11 	join() 	It returns a string which is the concatenation of all the strings specified in the given sequence.
# 12 	replace() 	It returns a copy of the string by replacing all occurrences of a particular substring with the specified one.
# 13 	decode() 	It is used to decode the specified string element-wise using the specified codec.
# 14 	encode() 	It is used to encode the decoded string element-wise.













# numpy.char.add() method example

import numpy as np   
print("Concatenating two string arrays:")  
print(np.char.add(['welcome','Hi'], [' to Javatpoint', ' read python'] ))  






# numpy.char.multiply() method example

import numpy as np   
print("Printing a string multiple times:")  
print(np.char.multiply("hello ",3))  





# numpy.char.center() method example

import numpy as np   
print("Padding the string through left and right with the fill char *");  
#np.char.center(string, width, fillchar)  
print(np.char.center("Javatpoint", 20, '*'))  







# numpy.char.capitalize() method example

import numpy as np   
print("Capitalizing the string using capitalize()...")  
print(np.char.capitalize("welcome to javatpoint"))  




# numpy.char.title() method example

import numpy as np   
print("Converting string into title cased version...")  
print(np.char.title("welcome to javatpoint"))  





# numpy.char.lower() method example

import numpy as np   
print("Converting all the characters of the string into lowercase...")  
print(np.char.lower("WELCOME TO JAVATPOINT"))  





# numpy.char.upper() method example

import numpy as np   
print("Converting all the characters of the string into uppercase...")  
print(np.char.upper("Welcome To Javatpoint"))  

    
    



# numpy.char.split() method example

import numpy as np   
print("Splitting the String word by word..")  
print(np.char.split("Welcome To Javatpoint"),sep = " ")  






# numpy.char.splitlines() method example

import numpy as np   
print("Splitting the String line by line..")  
print(np.char.splitlines("Welcome\nTo\nJavatpoint"))





# numpy.char.strip() method example

import numpy as np   
str = "     welcome to javatpoint     "  
print("Original String:",str)  
print("Removing the leading and trailing whitespaces from the string")  
print(np.char.strip(str))  






# numpy.char.join() method example

import numpy as np   
print(np.char.join(':','HM'))  



# numpy.char.replace() method example

import numpy as np  
str = "Welcome to Javatpoint"  
print("Original String:",str)  
print("Modified String:",end=" ")  
print(np.char.replace(str, "Welcome to","www."))  






# numpy.char.encode() and decode() method example

import numpy as np  
enstr = np.char.encode("welcome to javatpoint", 'cp500')  
dstr =np.char.decode(enstr, 'cp500')  
print(enstr)  
print(dstr)  

















# NumPy Mathematical Functions

# Numpy contains a large number of mathematical functions which can be used to perform various mathematical operations. The mathematical functions include trigonometric functions, arithmetic functions, and functions for handling complex numbers. Let's discuss the mathematical functions.
# Trigonometric functions

# Numpy contains the trigonometric functions which are used to calculate the sine, cosine, and tangent of the different angles in radian.

# The sin, cos, and tan functions return the trigonometric ratio for the specified angles. Consider the following example.











# Example

import numpy as np  
arr = np.array([0, 30, 60, 90, 120, 150, 180])  
print("\nThe sin value of the angles",end = " ")  
print(np.sin(arr * np.pi/180))  
print("\nThe cosine value of the angles",end = " ")  
print(np.cos(arr * np.pi/180))  
print("\nThe tangent value of the angles",end = " ")  
print(np.tan(arr * np.pi/180))  







# On the other hand, arcsin(), arccos(), and arctan() functions return the trigonometric inverse of the specified angles.

# The numpy.degrees() function can be used to verify the result of these trigonometric functions. Consider the following example.
# Example


import numpy as np  
arr = np.array([0, 30, 60, 90])  
print("printing the sin values of different angles")  
  
sinval = np.sin(arr*np.pi/180)  
  
print(sinval)  
print("printing the inverse of the sin")  
cosec = np.arcsin(sinval)  
  
print(cosec)  
  
print("printing the values in degrees")  
print(np.degrees(cosec))  
  
print("\nprinting the cos values of different angles")  
cosval = np.cos(arr*np.pi/180)  
  
print(cosval)  
print("printing the inverse of the cos")  
sec = np.arccos(cosval)  
print(sec)  
  
print("\nprinting the values in degrees")  
print(np.degrees(sec))  
  
print("\nprinting the tan values of different angles")  
tanval = np.tan(arr*np.pi/180)  
  
print(tanval)  
print("printing the inverse of the tan")  
cot = np.arctan(tanval)  
print(cot)  
  
print("\nprinting the values in degrees")  
print(np.degrees(cot))  










# Rounding Functions

# The numpy provides various functions that can be used to truncate the value of a decimal float number rounded to a particular precision of decimal numbers. Let's discuss the rounding functions.
# The numpy.around() function

# This function returns a decimal value rounded to a desired position of the decimal. The syntax of the function is given below.

#     numpy.around(num, decimals)  

# It accepts the following parameters.
# SN 	Parameter 	Description
# 1 	num 	It is the input number.
# 2 	decimals 	It is the number of decimals which to which the number is to be rounded. The default value is 0. If this value is negative, then the decimal will be moved to the left.

# Consider the following example.
# Example












import numpy as np  
arr = np.array([12.202, 90.23120, 123.020, 23.202])  
print("printing the original array values:",end = " ")  
print(arr)  
print("Array values rounded off to 2 decimal position",np.around(arr, 2))  
print("Array values rounded off to -1 decimal position",np.around(arr, -1))  





# The numpy.floor() function

# This function is used to return the floor value of the input data which is the largest integer not greater than the input value. Consider the following example.
# Example

import numpy as np  
arr = np.array([12.202, 90.23120, 123.020, 23.202])  
print(np.floor(arr))  




# The numpy.ceil() function

# This function is used to return the ceiling value of the array values which is the smallest integer value greater than the array element. Consider the following example.
# Example

import numpy as np  
arr = np.array([12.202, 90.23120, 123.020, 23.202])  
print(np.ceil(arr))  




# Numpy statistical functions

# Numpy provides various statistical functions which are used to perform some statistical data analysis. In this section of the tutorial, we will discuss the statistical functions provided by the numpy.
# Finding the minimum and maximum elements from the array

# The numpy.amin() and numpy.amax() functions are used to find the minimum and maximum of the array elements along the specified axis respectively.

# Consider the following example.


# Example

import numpy as np  
  
a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
  
print("The original array:\n")  
print(a)  
  
  
print("\nThe minimum element among the array:",np.amin(a))  
print("The maximum element among the array:",np.amax(a))  
  
print("\nThe minimum element among the rows of array",np.amin(a,0))  
print("The maximum element among the rows of array",np.amax(a,0))  
  
print("\nThe minimum element among the columns of array",np.amin(a,1))  
print("The maximum element among the columns of array",np.amax(a,1))  




# numpy.ptp() function

# The name of the function numpy.ptp() is derived from the name peak-to-peak. It is used to return the range of values along an axis. Consider the following example.
# Example

import numpy as np  
  
a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
  
print("Original array:\n",a)  
  
print("\nptp value along axis 1:",np.ptp(a,1))  
  
print("ptp value along axis 0:",np.ptp(a,0))  















# numpy.percentile() function

# The syntax to use the function is given below.

#     numpy.percentile(input, q, axis)  

# It accepts the following parameters.

#     input: It is the input array.
#     q: It is the percentile (1-100) which is calculated of the array element.
#     axis: It is the axis along which the percentile is to be calculated.

# Consider the following example.
# Example





import numpy as np  
  
a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
  
print("Array:\n",a)  
  
print("\nPercentile along axis 0",np.percentile(a, 10,0))  
  
print("Percentile along axis 1",np.percentile(a, 10, 1))  

















# Calculating median, mean, and average of array items
# The numpy.median() function:

# Median is defined as the value that is used to separate the higher range of data sample with a lower range of data sample. The function numpy.median() is used to calculate the median of the multi-dimensional or one-dimensional arrays.
# The numpy.mean() function:

# The mean can be calculated by adding all the items of the arrays dividing by the number of array elements. We can also mention the axis along which the mean can be calculated.
# The numpy.average() function:

# The numpy.average() function is used to find the weighted average along the axis of the multi-dimensional arrays where their weights are given in another array.

# Consider the following example.
# Example






import numpy as np  
  
a = np.array([[1,2,3],[4,5,6],[7,8,9]])  
  
print("Array:\n",a)  
  
print("\nMedian of array along axis 0:",np.median(a,0))  
print("Mean of array along axis 0:",np.mean(a,0))  
print("Average of array along axis 1:",np.average(a,1))  






# NumPy Sorting and Searching

# Numpy provides a variety of functions for sorting and searching. There are various sorting algorithms like quicksort, merge sort and heapsort which is implemented using the numpy.sort() function.

# The kind of the sorting algorithm to be used in the sort operation must be mentioned in the function call.

# Let's discuss the sorting algorithm which is implemented in numpy.sort()














# SN 	Algorithm 	Worst case complexity
# 1 	Quick Sort 	O (n ^ 2)
# 2 	Merge Sort 	O (n * log(n))
# 3 	Heap Sort 	O (n * log(n))

# The syntax to use the numpy.sort() function is given below.

#     numpy.sort(a, axis, kind, order)  

# It accepts the following parameters.
# SN 	Parameter 	Description
# 1 	input 	It represents the input array which is to be sorted.
# 2 	axis 	It represents the axis along which the array is to be sorted. If the axis is not mentioned, then the sorting is done along the last available axis.
# 3 	kind 	It represents the type of sorting algorithm which is to be used while sorting. The default is quick sort.
# 4 	order 	It represents the filed according to which the array is to be sorted in the case if the array contains the fields.

# Consider the following example.
# Example







import numpy as np  
  
a = np.array([[10,2,3],[4,5,6],[7,8,9]])  
  
print("Sorting along the columns:")  
print(np.sort(a))  
  
print("Sorting along the rows:")  
print(np.sort(a, 0))  
  
data_type = np.dtype([('name', 'S10'),('marks',int)])  
  
arr = np.array([('Mukesh',200),('John',251)],dtype = data_type)  
  
print("Sorting data ordered by name")  
  
print(np.sort(arr,order = 'name'))  










# numpy.argsort() function

# This function is used to perform an indirect sort on an input array that is, it returns an array of indices of data which is used to construct the array of sorted data.

# Consider the following example.
# Example

import numpy as np  
  
a = np.array([90, 29, 89, 12])  
  
print("Original array:\n",a)  
  
sort_ind = np.argsort(a)  
  
print("Printing indices of sorted data\n",sort_ind)  
  
sort_a = a[sort_ind]  
  
print("printing sorted array")  
  
for i in sort_ind:  
    print(a[i],end = " ")  








# numpy.lexsort() function

# This function is used to sort the array using the sequence of keys indirectly. This function performs similarly to the numpy.argsort() which returns the array of indices of sorted data.

# Consider the following example.
# Example

import numpy as np  
  
a = np.array(['a','b','c','d','e'])  
  
b = np.array([12, 90, 380, 12, 211])  
  
ind = np.lexsort((a,b))  
  
print("printing indices of sorted data")  
  
print(ind)  
  
print("using the indices to sort the array")  
  
for i in ind:  
    print(a[i],b[i])  














# numpy.nonzero() function

# This function is used to find the location of the non-zero elements from the array.

# Consider the following example.
# Example

import numpy as np  
  
b = np.array([12, 90, 380, 12, 211])  
  
print("printing original array",b)  
  
print("printing location of the non-zero elements")  
  
print(b.nonzero())  


















# numpy.where() function

# This function is used to return the indices of all the elements which satisfies a particular condition.

# Consider the following example.
# Example

import numpy as np  
  
b = np.array([12, 90, 380, 12, 211])  
  
print(np.where(b>12))  
  
c = np.array([[20, 24],[21, 23]])  
  
print(np.where(c>20))  











# NumPy Copies and Views

# The copy of an input array is physically stored at some other location and the content stored at that particular location is returned which is the copy of the input array whereas the different view of the same memory location is returned in the case of view.

# In this section of the tutorial, we will consider the way by which, the different copies and views are generated from some memory location.
# Array Assignment

# The assignment of a numpy array to another array doesn't make the direct copy of the original array, instead, it makes another array with the same content and same id. It represents the reference to the original array. Changes made on this reference are also reflected in the original array.

# The id() function returns the universal identifier of the array similar to the pointer in C.

# Consider the following example.
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
  
print("Original Array:\n",a)  
  
print("\nID of array a:",id(a))  
  
b = a   
  
print("\nmaking copy of the array a")  
  
print("\nID of b:",id(b))  
  
b.shape = 4,3;  
  
print("\nChanges on b also reflect to a:")  
print(a)  

















# ndarray.view() method

# The ndarray.view() method returns the new array object which contains the same content as the original array does. Since it is a new array object, changes made on this object do not reflect the original array.

# Consider the following example.
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
  
print("Original Array:\n",a)  
  
print("\nID of array a:",id(a))  
  
b = a.view()  
  
print("\nID of b:",id(b))  
  
print("\nprinting the view b")  
print(b)  
  
b.shape = 4,3;  
  
print("\nChanges made to the view b do not reflect a")  
print("\nOriginal array \n",a)  
print("\nview\n",b)  














# ndarray.copy() method

# It returns the deep copy of the original array which doesn't share any memory with the original array. The modification made to the deep copy of the original array doesn't reflect the original array.

# Consider the following example.
# Example

import numpy as np  
  
a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
  
print("Original Array:\n",a)  
  
print("\nID of array a:",id(a))  
  
b = a.copy()  
  
print("\nID of b:",id(b))  
  
print("\nprinting the deep copy b")  
print(b)  
  
b.shape = 4,3;  
  
print("\nChanges made to the copy b do not reflect a")  
print("\nOriginal array \n",a)  
print("\nCopy\n",b)  


























# NumPy Matrix Library

# NumPy contains a matrix library, i.e. numpy.matlib which is used to configure matrices instead of ndarray objects.
# numpy.matlib.empty() function

# This function is used to return a new matrix with the uninitialized entries. The syntax to use this function is given below.

#     numpy.matlib.empty(shape, dtype, order)  

# It accepts the following parameter. 





#     shape: It is the tuple defining the shape of the matrix.
#     dtype: It is the data type of the matrix.
#     order: It is the insertion order of the matrix, i.e. C or F.

# Consider the following example.
# Example




import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.empty((3,3)))  








# numpy.matlib.zeros() function

# This function is used to create the matrix where the entries are initialized to zero.

# Consider the following example.
# Example

import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.zeros((4,3)))  













# numpy.matlib.ones() function

# This function returns a matrix with all the elements initialized to 1.

# Consider the following example.
# Example

import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.ones((2,2)))  















# numpy.matlib.eye() function

# This function returns a matrix with the diagonal elements initialized to 1 and zero elsewhere. The syntax to use this function is given below.

#     numpy.matlib.eye(n, m, k, dtype)   

# It accepts the following parameters.

#     n: It represents the number of rows in the resulting matrix.
#     m: It represents the number of columns, defaults to n.
#     k: It is the index of diagonal.
#     dtype: It is the data type of the output

# Consider the following example.
# Example

import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.eye(n = 3, M = 3, k = 0, dtype = int))  




# numpy.matlib.identity() function

# This function is used to return an identity matrix of the given size. An identity matrix is the one with diagonal elements initializes to 1 and all other elements to zero.

# Consider the following example.
# Example

import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.identity(5, dtype = int))  







# numpy.matlib.rand() function

# This function is used to generate a matrix where all the entries are initialized with random values.

# Consider the following example.
# Example

import numpy as np  
  
import numpy.matlib  
  
print(numpy.matlib.rand(3,3))  























# NumPy Linear Algebra

# Numpy provides the following functions to perform the different algebraic calculations on the input data.
# SN 	Function 	Definition
# 1 	dot() 	It is used to calculate the dot product of two arrays.
# 2 	vdot() 	It is used to calculate the dot product of two vectors.
# 3 	inner() 	It is used to calculate the inner product of two arrays.
# 4 	matmul() 	It is used to calculate the matrix multiplication of two arrays.
# 5 	det() 	It is used to calculate the determinant of a matrix.
# 6 	solve() 	It is used to solve the linear matrix equation.
# 7 	inv() 	It is used to calculate the multiplicative inverse of the matrix.
















# numpy.dot() function

# This function is used to return the dot product of the two matrices. It is similar to the matrix multiplication. Consider the following example.
# Example

import numpy as np  
a = np.array([[100,200],[23,12]])  
b = np.array([[10,20],[12,21]])  
dot = np.dot(a,b)  
print(dot)  











# numpy.vdot() function

# This function is used to calculate the dot product of two vectors. It can be defined as the sum of the product of corresponding elements of multi-dimensional arrays.

# Consider the following example.
# Example

import numpy as np  
a = np.array([[100,200],[23,12]])  
b = np.array([[10,20],[12,21]])  
vdot = np.vdot(a,b)  
print(vdot)  













# numpy.inner() function

# This function returns the sum of the product of inner elements of the one-dimensional array. For n-dimensional arrays, it returns the sum of the product of elements over the last axis.

# Consider the following example.
# Example

import numpy as np  
a = np.array([1,2,3,4,5,6])  
b = np.array([23,23,12,2,1,2])  
inner = np.inner(a,b)  
print(inner)  











# numpy.matmul() function

# It is used to return the multiplication of the two matrices. It gives an error if the shape of both matrices is not aligned for multiplication. Consider the following example.
# Examp[le

import numpy as np  
a = np.array([[1,2,3],[4,5,6],[7,8,9]])  
b = np.array([[23,23,12],[2,1,2],[7,8,9]])  
mul = np.matmul(a,b)  
print(mul)  









# numpy determinant

# The determinant of the matrix can be calculated using the diagonal elements. The determinant of following 2 X 2 matrix

# A       B
# C       D

# can be calculated as AD - BC.

# The numpy.linalg.det() function is used to calculate the determinant of the matrix. Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2],[3,4]])  
print(np.linalg.det(a))  













# numpy.linalg.solve() function

# This function is used to solve a quadratic equation where values can be given in the form of the matrix.

# The following linear equations

# 3X + 2 Y + Z = 10   
# X + Y + Z = 5  



# can be represented by using three matrices as:

#     3   2   1  
#     1   1   1  
#     X  
#     Y  
#     Z  and  
#     10  
#     5.  

# The two matrices can be passed into the numpy.solve() function given as follows.
# Example

import numpy as np  
a = np.array([[1,2],[3,4]])  
b = np.array([[1,2],[3,4]])  
print(np.linalg.solve(a, b))  





# numpy.linalg.inv() function

# This function is used to calculate the multiplicative inverse of the input matrix. Consider the following example.
# Example

import numpy as np  
a = np.array([[1,2],[3,4]])  
print("Original array:\n",a)  
b = np.linalg.inv(a)  
print("Inverse:\n",b)  





# NumPy Matrix Multiplication in Python

# Multiplication of matrix is an operation which produces a single matrix by taking two matrices as input and multiplying rows of the first matrix to the column of the second matrix. Note that we have to ensure that the number of rows in the first matrix should be equal to the number of columns in the second matrix.







# In Python, the process of matrix multiplication using NumPy is known as vectorization. The main objective of vectorization is to remove or reduce the for loops which we were using explicitly. By reducing 'for' loops from programs gives faster computation. The build-in package NumPy is used for manipulation and array-processing.

# These are three methods through which we can perform numpy matrix multiplication.

#     First is the use of multiply() function, which perform element-wise multiplication of the matrix.
#     Second is the use of matmul() function, which performs the matrix product of two arrays.
#     Last is the use of the dot() function, which performs dot product of two arrays.












# Example 1: Element-wise matrix multiplication

import numpy as np  
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)  
result=np.multiply(array1,array2)  
result  

# In the above code

#     We have imported numpy with alias name np.
#     We have created an array1 and array2 using numpy.array() function with dimension 3.
#     We have created a variable result and assigned the returned value of np.multiply() function.
#     We have passed both the array array1 and array2 in np.multiply().
#     Lastly, we tried to print the value of the result.

# In the output, a three-dimensional matrix has been shown whose elements are the result of the element-wise multiplication of both array1 and array2 elements.






# Example 2: Matrix product

import numpy as np  
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)  
result=np.matmul(array1,array2)  
result  


# In the above code

#     We have imported numpy with alias name np.
#     We have created array1 and array2 using numpy.array() function with dimension 3.
#     We have created a variable result and assigned the returned value of the np.matmul() function.
#     We have passed both the array array1 and array2 in np.matmul().
#     Lastly, we tried to print the value of the result.

# In the output, a three-dimensional matrix has been shown whose elements are the product of both array1 and array2 elements.
# Example 3: Dot product

# These are the following specifications for numpy.dot:

#     When both a and b are 1-D (one dimensional) arrays-> Inner product of two vectors (without complex conjugation)
#     When both a and b are 2-D (two dimensional) arrays -> Matrix multiplication
#     When either a or b is 0-D (also known as a scalar) -> Multiply by using numpy.multiply(a, b) or a * b.
#     When a is an N-D array and b is a 1-D array -> Sum product over the last axis of a and b.
#     When a is an N-D array and b is an M-D array provided that M>=2 -> Sum product over the last axis of a and the second-to-last axis of b:
#     Also, dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

import numpy as np  
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)  
result=np.dot(array1,array2)  
result  

# In the above code

#     We have imported numpy with alias name np.
#     We have created array1 and array2 using numpy.array() function with dimension 3.
#     We have created a variable result and assigned the returned value of the np.dot() function.
#     We have passed both the array array1 and array2 in np.dot().
#     Lastly, we tried to print the value of the result.

# In the output, a three-dimensional matrix has been shown whose elements are the dot product of both array1 and array2 elements.






















