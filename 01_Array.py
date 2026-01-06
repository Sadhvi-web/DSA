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

# Add elements to array
# Append method
# from array import *
# a=array("i",[1,2,3,4])
# a.append(5)
# print(a)

# Insert method
# from array import *
# a=array("i",[1,2,3,4])
# a.Insert(1,200)
# print(a)

# extend method
# from array import *
# a=array("i",[1,2,3,4])
# b=array("i",[100,200,300,400])
# a.extend(b)
# print(a)


# Remove Array Elements
# Remove first occurence using REmove method
# from array import *
# a=array("i",[1,2,3,4])
# print("Before Removing",a)
# a.remove(4)
# print("After Removing",a)

# Remove items from specific index
# from array import *
# a=array("i",[1,2,3,4])
# print("Before Removing",a)
# a.pop(2)
# print("After Removing",a)


# Copy Array
# copy array using assignment operator
# from array import *
# a=array("i",[1,2,3,4])
# b=a
# print(b)
# print("id of a : ",id(a),"id of b : ",id(b))

# Copy Arrays Using Deep Copy
# from array import *
# import copy
# a=array("i",[1,2,3,4])
# b=copy.deepcopy(a)
# print("copied array : ",b)



# Reverse array
# using Slicing operation
# from array import *
# arr1 = array("i",[10,20,30,40,50])
# print("Original array: ",arr1)
# rev_arr = arr1[::-1]
# print("Reversed array: ",rev_arr)

# using reverse function
# from array import *
# arr1 = array("i",[10,20,30,40,50])
# print("Original array: ",arr1)

# new_arr1 = arr1.tolist()

# new_arr1.reverse()
# rev_arr = array('i',new_arr1)
# print("Reversed array: ",rev_arr)

# using reversed function
# from array import *
# arr1 = array("i",[10,20,30,40,50])
# print("Original array: ",arr1)

# new_arr1 = list(reversed(arr1))
# rev_arr = array("i",new_arr1)
# print("Reversed array: ",rev_arr)

# Using for loop
# from array import *
# arr1 = array("i",[10,20,30,40,50])
# print("Original array: ",arr1)

# rev_arr = array("i")
# for i in range(len(arr1)-1,-1,-1):
#     rev_arr.append(arr1[i])
# print("Reversed array: ",rev_arr)




# Sort array
# Method 1
# from array import *
# a1 = array("i",[10,5,15,4,6,20,9])
# print("Original array :- ",a1)

# for i in range(0,len(a1)):
#     for j in range(1,len(a1)):
#         if a1[i]>a1[j]:
#             temp = a1[i]
#             a1[i] = a1[j]
#             a1[j] = temp
# print("Sorted Array :- ",a1)

# Method 2
# from array import *
# a1 = array("i",[10,5,15,4,6,20,9])
# print("Original array :- ",a1)

# sorted_List = a1.tolist()
# sorted_List.sort()

# sorted_array = array("i",sorted_List)
# print("Sorted Array :- ",sorted_array)

# Method 3
# from array import *
# a1 = array("i",[10,5,15,4,6,20,9])
# print("Original array :- ",a1)
# sorted_array = sorted(a1)
# print("Sorted Array :- ",sorted_array)



# Join arrays
# Method 1
# from array import *
# a1 = array("i",[10,5,15,4,6,20,9])
# b1=array("i",[100,200,300,400])

# for i in range(len(b1)):
#     a1.append(b1[i])
# print(a1)

# Method 2
# from array import *
# a1 = array("i",[10,5,15,4,6,20,9])
# b1=array("i",[100,200,300,400])

# a1.extend(b1)
# print(a1)