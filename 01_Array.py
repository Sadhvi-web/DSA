# 1. Initializing Array in Python

# Method1
# import array
# a1 = array.array("i",[1,2,310,20,30])

# Method 2
# import array as arr
# a1 = arr.array("i",[1,2,3,10,20,30])

# Method 3
# from array import *
# a1 = array("i",[1,2,3,10,20,30])

# Method 4
# import numpy as np
# a1 = np.array([1,2,3,10,20,30])


# 2. Accessing elements of array

# Method1
# import numpy as np
# a1 = np.array([1,2,3,10,20,30])
# print(a1[0])
# print(a1[1])
# print(a1[2])
# print(a1[3])
# print(a1[4])
# print(a1[5])

# Method 2
# import numpy as np
# a1 = np.array([1,2,3,10,20,30])
# for vals in a1:
#     print(vals)

# Method 3
# import numpy as np
# a1 = np.array([1,2,3,10,20,30])
# vals=0
# while(vals<len(a1)):
#     print(a1[vals])
#     vals += 1


# 3. taking user input in array
# from array import * 
# a1 = array("i",[])

# n=int(input("Enter the length of array : "))

# for i in range(n):
#     x = int(input("Enter the values: "))
#     a1.append(x)
# print(a1)


# 4.For searching element in an array
# from array import * 
# a1 = array("i",[1,2,3,4])
# elem_to_search = 4

# for i in range(len(a1)):
#     if a1[i] == elem_to_search:
#         print(f"{elem_to_search} found at index {i}")


# 5. for searching element in an array taking input by user
# from array import * 
# a1 = array("i",[])

# n=int(input("Enter the length of array : "))

# for i in range(n):
#     x = int(input("Enter the values: "))
#     a1.append(x)
# print(a1)
# vals = int(input("Enetr the element you want to search : "))

# ind = 0
# for elem in a1:
#     if elem == vals:
#         print("Element is at index no. : ",ind)
#         break
#     ind += 1