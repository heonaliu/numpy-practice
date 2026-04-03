import numpy as np

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teens = ages[ages<18]

print(teens)

new_age = np.sort(ages, axis=0)
print(new_age)

arr = np.array([1,2,2,3,5,6])
print(np.histogram(arr, bins=3))
