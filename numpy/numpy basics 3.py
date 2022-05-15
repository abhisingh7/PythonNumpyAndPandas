import numpy as np

# Print random number arrays in a fixed range.
print('Print random number arrays in a fixed range...')

rand_arr = np.random.randint(1,15,4)
print('\n4 random number from 1 to 15 ',rand_arr)

rand_arr2 = np.random.randint(1,100,20)
print('\n20 random number from 1 to 100 ',rand_arr2)

rand_arr3 = np.random.randint([2,3]) # First value less than 2 and second value less than 3
print('\nrandom number array in a fixed range',rand_arr3)

# count the occurence of each element of array in a sequence.
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print('\nOccurence of each element:', np.bincount(arr))

# Adding the element of 2 arrays
array1= np.array([1,2,3])
array2= np.array([1,2,3])
array3= array1 + array2
print("\nAdding 2 arrays:", array3)
array3= array1 * array2
print("\nMultiplying 2 arrays:", array3)

# Square the elements in an array by using ‘**’.
array1= np.array([1,2,3])
print("\nSquaring the element of array:",array1**2)

# Using power() method in numpy array
print("\nUsing power() method with numpy array:",np.power(array1,3))

# Matrix multiplication of two 2d array
A = np.array([[3,2],[0,1]])
B = np.array([[3,1],[2,1]])
print("\nMatrix multiplication using @", A@B)

# Changing array datatype using numpy.astype()
print("\nChanging array datatype using numpy.astype()....")
arr = np.array([1.3, 2.2, 3.1])
print("\narray:",arr)
print("Current datatype",arr.dtype)
arr = arr.astype('i')  # converting float into integer
print("After changing array datatype from float to integer:",arr)
print("New datatype",arr.dtype)

# view vs copy
print("\n view() vs copy() method....")
arr = np.array([20,30,50,70])
a = arr.copy()
b = arr.view()

#changing a value in copy array
a[0] = 5

print("\nOriginal array:",arr)
print("Copied array:",a)

#changing a value in view array
b[0] = 5
print("\nOriginal array:",arr)
print("View array:",b)

# Note: Copy create an independent object while view assign the same object.