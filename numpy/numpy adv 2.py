import numpy as np

a = np.arange(12).reshape(3,4)
print("Array: \n",a)

# Printing each element in row wise using flatten() method
print("printing flatten array by iteration")
for cell in a.flatten():
    print(cell)
print()
# Printing each element in row wise using nditer() method

print("printing flatten array each element using nditer in c order")
for x in np.nditer(a, order='C'):
    print(x)
print()

# if we want to print each element column wise (fortran order)

print("printing flatten array each element using nditer in fortran order")
for x in np.nditer(a, order='F'):
    print(x)
print()

# If we want to print whole column in fortran order we use flags in argument.
print("printing flatten array whole column using nditer in fortran order")
for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)
print()

# If we are iterating through array and want to modify element, we use op_flags in argument
print("If we are iterating through array and want to modify element")
print("array: \n",a)
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*x # Each element will be squared.
print("each element of array will be squared")
print(a)
print()


# Iterating through two arrays simultaneously
print("Iterating two arrays simultaneously")
print("Array a: \n",a)
print()
b = np.arange(3,15,4).reshape(3,1)
print("Array b: \n",b)
print("\n iterating a and b both")

# Note: for this kind of iteration either the shape of both arrays should be same
# or one of the dimension of both array must be equal. Otherwise it will give value error
# that "operands could not be broadcast together with different shapes".
# In our case rows are equal
for x,y in np.nditer([a,b]):
    print(x,y)