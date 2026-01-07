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