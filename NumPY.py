import numpy as np
a = np.array([2,3,4])
print(a)
print(type(a))

#Both array length should be same 
ar1 = np.array([1,2,3,4,5])
ar2 = np.array([6,7,8,9,10])
result1 = ar1+ar2
print(result1)
print(ar1.dtype) #type eka print wenne int64 - means computer id bit 64

result2 = ar1-ar2
print(result2)
result3 = ar1*ar2
print(result3)
result4 = ar1/ar2
print(result4)

#squre root
result_sqrt = np.sqrt(ar1)
#summation
result_sum = np.sum(ar1)
#Mean
result_mean = np.mean(ar2)

maximum = np.max(ar1)
minimum = np.min(ar2)

ar3 = np.array([[1,2,3],[4,5,6]])
print(ar3)
print(ar3.size)
print(ar3.shape) #2,3 2 rows and 3 cols

ar4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(ar4)#tuple widihata return krnne
print(ar4.size)#number of elements
print(ar4.shape) #2, 2, 3       2-> outer most eke element 2i mulma[] 2,3->ilha[] thiyenne 2d array ekak kiyna ekak
print(ar4.ndim)#number of dimensions 3


#NumPy array indexing
array1 = np.array([1,2,3,4])
print(array1[2])
array2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element in 1st row:',array2[0,1])

"""
creat a 2d munPY array which has dimention 4*5 which contains the numbers 1 to 20 
perform the following on this array
    - add 10 to every elemet
    - multipy every element by 2 
    - calculate the squre of each element 
"""

array = np.array([[2,13,15,5,7],[8,9,12,14,3],[18,14,4,3,5],[16,17,13,2,1]])
print(array.shape)
print(array ** 2)
print(array + 10)
print(array * 2)

#Boolean arrays
#In numPy array without using for loops everything will applied to the each element
ar5 = np.array([10,20,30,40,50])
condition = ar5 > 25
print(condition)
filtered = ar5[condition]#element will be printed as a array
print(filtered)
#In single step
filterd_array = ar5[ar5>25]
print(filterd_array)

#Combine multiple conditions
filterd_combined = ar5[(ar5>20) & (ar5<45)]
print(filterd_combined)

#Inbuild functions for array initialization
print('Array Initialization')
array1 = np.zeros(5)
print(array1)#[0. 0. 0. 0. 0.]
array2 = np.zeros((2,3))
print(array2)#[[0. 0. 0.][0. 0. 0.]]
#Meka interger0 wenuwata folat enna one nm np.zeros(shape, dtype=float)

array3 = np.full(4,7)
print(array3)#[7 7 7 7]
array4 = np.full((2,3),8)
print(array4)#[[8 8 8],[8 8 8]]

array4 = np.empty((2,3))
print(array4)#garbage value ekak assign krnwa meka speed avoid overhead of initialization
"""
[[4.65522264e-310 0.00000000e+000 0.00000000e+000]
 [0.00000000e+000 0.00000000e+000 0.00000000e+000]]
"""

"""
#create a 1d numPY array with values from 1 to 20 use boolean index into extract all even numbers 
ar1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
filterd_array1 = ar1[ar1%2==0]
print(filterd_array1)

#create a numPY array with elemets 10,20,30,40,50 use boolean indexing to axtract all elements grater than the mean of the array
ar2 = np.array([10,20,30,40,50])
mean = np.mean(ar2)
filterd_array2 = ar2[ar2>mean]
print(filterd_array2)
"""