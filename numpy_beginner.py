import numpy as np

# Creating numpy array:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [
                  [9, 10, 11, 12], [13, 14, 15, 16]]])

# Check the dimension of an array

print(arr_2d.ndim)

# Initialize a 5-d numpy array
arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print(arr_5d)
print('number of dimensions :', arr_5d.ndim)

# indexing

ele_row2_col3 = arr_2d[1, 2]
print(f'element in the third colunm of the secon row {ele_row2_col3}')

# Negative indexing
row2_col3_ele = arr_2d[1, -2]
print(f'element in the third colunm of the secon row {row2_col3_ele}')

# Slicing
ele_2_to_5 = arr[1:4]
print(f'second element to 5th element {ele_2_to_5}')

# Slicing with step
ele_step_2 = arr[::2]
print(f'second element to 5th element {ele_step_2 }')  # [1,3,5,7]

# Slicing a 2D array
ele_2D_sliced = arr_2d[1, ::2]
print(f'second element slice with a step of 2: {ele_2D_sliced }')  # [5,7]

elements_index2 = arr_2d[:, 2]
print(f'all element in index two: {elements_index2 }')  # [3,7]

elements_index2 = arr_2d[:, 2]
print(f'all element in index two: {elements_index2 }')  # [3,7]

slice_2d_arr = arr_2d[:, 1:3]
print(f'2D array index 1-3, 3 not included: {slice_2d_arr}')  # [[2,3],[6,7]]
