import numpy as np

a = np.array([5,6,7])
print("array: ",a)
print("Shape of array: ", a.shape)

# printing single value
print("Printing single element from array")
print(a[0])
print(a[1])

# dimensions of numpy array
print("Dimension: ",a.ndim)

# size of single element
print("Size of single element: ",a.itemsize)

# datatype of array elements
print("datatype: ",a.dtype)

a = np.array([[1,2], [3,4], [5,6]])
print("Array: ",a)
# dimensions of numpy array
print("Dimension: ",a.ndim)

# Changing datatype of array to float
print("Changing array to float datatype")
a2 = np.array([[1,2], [3,4], [5,6]], dtype=float)
print(a2)
print("Size of single element: ",a2.itemsize)
print("total no. of elements: ",a2.size)
print("Shape of array: ", a2.shape)

#Changing datatype of array to complex
print("Changing array to complex datatype")
a3 = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print(a3)

# creating zeros or ones array by providing their dimensions
print("Printing array of zeros...")
print(np.zeros((3,4)))

print("Printing array of ones...")
print(np.ones((3,4)))

# creating 2d array with 1 as diagonal values, rest are zeros.
print('Printing 2d array with 1 as diagonal values, rest are zeros...')
arr = np.eye(4)
print('diaglonal values : ',arr)

# creating 2d array with some other numbers as diagonal values, rest are zeros.
print('Printing 2d array with some other numbers as diagonal values, rest are zeros...')
arr = np.diag([1,2,3,4])
print('diaglonal values : ',arr)


# Using arange for creating array for fixed number of elements => arange(start, end, step).
print("using arange method...")
print(np.arange(1,5))
print(np.arange(1,5,2))

# creating a linearly spaced array => linspace(start, end, num).
print("using linspace method...")
print(np.linspace(1,5,5))
print(np.linspace(1,5,10))

# reshaping array
print("Reshaping array...")
a = np.array([[1,2], [3,4], [5,6]])
print("Array: ",a)
print("Array current shape: ",a.shape)
print("Array after reshape: ", a.reshape(2,3))
print("Array after reshape: ", a.reshape(6,1))

# Flatening multi-dimensional array to one dimension
print("array flatening: ", a.ravel())

# Note: reshape() and ravel() never change the original array. They create and return new object.

print("Array: ",a)

# min and max
print("min and max value of array....")
print("min: ",a.min())
print("max: ", a.max())

# sum of all elements of array
print("sum of array..")
print("sum: ",a.sum())

# axis = 0 => column and axis = 1 => rows
print("Array: ",a)
print("sum of columns (axis=0): ",a.sum(axis=0))
print("sum of rows (axis=1): ",a.sum(axis=1))

#  sqrt and standard deviation of array
print("Array: ",a)
print("square root: ",np.sqrt(a))
print("Standard deviation: ",np.std(a))

# matrix product
a = np.array([[1,1],[0,1]])
b = np.array([[5,6],[7,8]])
print("Array a : ",a)
print("Array b : ",b)
print("matrix product of a and b", a.dot(b))