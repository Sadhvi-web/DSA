# Array Exercises
# 1. Python program to find the largest number in an array
from array import *
a = array("i",[10,5,15,4,6,20,9])
print(a)
largest = a[0]

for i in range(1,len(a)):
    if a[i] > largest:
        largest = a[i]
print("Largest number :- ",largest)


# 2.Python program to store all even numbers from an array in another array
from array import *
a = array("i",[10,5,15,4,6,20,9])
print(a)
b = array("i")

for i in range(0,len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
    
print("Even numbers:- ",b)


# 3. Python program to find the average of all numbers in a Python array
# Method 1
from array import *
a = array("i",[10,5,15,4,6,20,9])
print(a)

s = 0
for i in range(0,len(a)):
    s += a[i]

avg = s/len(a)
print("Average of Array = ",avg)

# Method 2
from array import *
a = array("i",[10,5,15,4,6,20,9])
print(a)

avg = sum(a)/len(a)
print("Average of Array = ",avg)
