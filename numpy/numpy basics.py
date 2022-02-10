import numpy as np
import time
import sys

# Converting a list into array
a = np.array([1,2,3])
print(a)

# Comparing size of list vs numpy array
l = range(1000)
print(sys.getsizeof(5)*len(l))

array  = np.arange(1000)
print(array.size*array.itemsize)

# Comparing time of list operations vs numpy array operations

SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python list timing
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print(f"Python list took: {(time.time() - start)*1000} milliseconds") # Time calc. in milliseconds

# numpy array timing
start = time.time()
result = a1+a2 # We can do all mathematical operations like +-*/ on numpy array
print(f"numpy took: {(time.time() - start)*1000} milliseconds")