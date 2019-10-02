

##converting a nested list into a flat list 
def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x)
                for x in li), [])

print(flatten([1, 2, [3], [4, [5, 6]]]))



##method 1.
##Flatten List using Inbuilt reduce Function


import functools
import operator
li = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
flat_list = functools.reduce(operator.concat, li)
print(flat_list)



##method 2.
##Flatten List Using List Compression

li = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]

flat_list = [item for sublist in li for item in sublist]
print(flat_list)



##method 3.
##Flatten List Using NumPy

## first install the python library to use 
## use the command.
## "pip install numpy"



##import your library.
import numpy
## create yout list
li = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]

flat_list = list(numpy.concatenate(li).flat)
print(flat_list)