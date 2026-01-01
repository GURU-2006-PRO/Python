# printing the reverse with using numpy
import numpy

def arrays(arr):
     # convert list of strings to numpy array of floats
    arr = numpy.array(arr, dtype=float)
    # reverse the array
    return arr[::-1]
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)