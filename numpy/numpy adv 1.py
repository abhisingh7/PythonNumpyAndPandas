import numpy as np

# 1. Using subscipting and slicing on arrays
print("array subscripting and slicing...")
a = np.array([6,7,8])
print("array subscripting: ",a[-1])
print("array slicing: ",a[0:2])

print()

print("array subscripting and slicing on 2d array...")
a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print("Array: ",a)
print("picking specific element: \n",a[1,2]) # First row and second column element

print("Array slicing for specific elements: \n",a[0:2,2]) # a[row slicing, column slicing]
print("Array slicing for specific elements: \n",a[-1,0:2]) # a[row slicing, column slicing]
print("Array slicing for specific elements: \n",a[:,1:3]) # all rows and 2nd and 3rd column elements

print()

# 2. Iteration on arrays
print("Iteration on arrays...")
a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print("Array: \n",a)

print("Iterating...")
for row in a:
    print(row)

# iterating single element by flatening array.
print("Iterating for single element from array")
for cell in a.flat: # a.ravel() also works here
    print(cell)

# 3. Stacking together two arrays
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print("Array a: \n",a)
print("Array b: \n",b)

print("Stacking a and b vertically: \n",np.vstack((a,b))) # Note: vstack take tuple as argument
print("Stacking a and b horizontally: \n",np.hstack((a,b))) # Note: vstack take tuple as argument

print()
# 4. Spliting bigger array into smaller ones
print("Spliting bigger array into smaller ones...")
a = np.arange(30).reshape(2,15)
print("Array: \n",a)

print("Using hsplit()")
print("\n",np.hsplit(a,3)) # (axis=0 => column) Vertically splitting into 3 equal sized arrays
result = np.hsplit(a,3)
print("\n",result[0])
print("\n",result[1])
print("\n",result[2])


print("Using vsplit()")
print("Array: \n",a)
print("\n",np.vsplit(a,2)) # (axis = 1 => row)Horizontally splitting into 2 equal sized arrays
result = np.vsplit(a,2)
print("\n",result[0])
print("\n",result[1])

print()
# 5. Indexing with boolean array
print("Indexing with boolean array...")
a = np.arange(12).reshape(3,4)
print("Array: \n",a)

b = a > 4 #comparing each element greater than 4 or not
print("Array b: \n",b)

print("\n",a[b]) # wherever b is true it returns value of those elements

# IF we want to replace the element with some other value then we can do this assignment
print("Assigning some different value if found True for a>4")
a[b]= -1
print("\n",a)