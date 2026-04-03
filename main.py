import numpy as np

# my_list = [1,2,3,4]
# array = np.array([1,2,3,4])

# print(array*2)

# array = np.array('A')
# print(array.ndim) 

# array = np.array([[[1,2,3], [3,4,5]],[[6,7,8],[9,11,12]]])
# print(array)
# print(array.shape)

## slicing


# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16],
#                   ])

# #print(array[:,1:2])
# print(array[0:2, 2:4])

array = np.array([1,2,3])

#scalar
print(array+1)

#vectorized
radii = np.array([1,2,3])
area = radii**2 * np.pi

print(area)

#element-wise arithmetic
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
# print(array2*array1)

scores = np.array([78,89,55,99,86])