# Selection Sort
from array import *
nums = array("i",[5,7,8,4,1,6,9,2])

def Selection_sort(nums):
    for i in range(0,len(nums)):
        min_ind = i
        for j in range(i+1 ,len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i],nums[min_ind] = nums[min_ind],nums[i]

Selection_sort(nums)
print(nums)

# In descending order
from array import *
nums = array("i",[5,7,8,4,1,6,9,2])
def Selection_sort_desc(nums):
    for i in range(0,len(nums)):
        max_ind = i
        for j in range(i+1 ,len(nums)):
            if nums[j] > nums[max_ind]:
                max_ind = j
        nums[i],nums[max_ind] = nums[max_ind],nums[i]

Selection_sort_desc(nums)
print(nums)


# Bubble Sort
# for worst and average case
from array import *
nums = array("i",[5,7,8,4,1,6,9,2])

def Bubble_Sort(nums):
    n= len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

Bubble_Sort(nums)
print(nums)

# For best case
from array import *
nums = array("i",[1, 2, 5, 6, 7, 8, 9])

def Bubble_Sort_best(nums):
    n= len(nums)
    
    for i in range(n-2,-1,-1):
        is_Swapped = False
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_Swapped = True
    if is_Swapped == False:
        print("Not Swapped")
        return
Bubble_Sort_best(nums)
print(nums)


# Insertion Sort
from array import *
nums = array("i",[5,7,8,40,1,6,9,2])

def Insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1

        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key

Insertion_sort(nums)
print(nums)



# Merge sort
# Mergetwo sorted array
from array import *
left = array("i",[1,2,3,4])
right = array("i", [1,1,3,4,5,6,7])

def merge_sorted_array(left,right):
    result=[]
    i,j =0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
    
print(merge_sorted_array(left,right))


# Merge sort an unsorted array(Real merge sort)
from array import *
arr = array("i",[3,1,2,4,1,5,2,6,4])

def merge_sorted_array(left,right):
    result=[]
    i,j =0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
    
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return(merge_sorted_array(left,right))

print(merge_sort(arr))
