# Question 1 :- find the largest element element in an array
# method 1
from array import *
a= array('i',[12,45,21,45,63,54,87,21])

largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        i+=1
print(largest)
# T.C - O(N)
# S.C - O(1)

# Method 2
from array import *
a= array('i',[45,89,21,63,52,74,85,25])

largest = float('-inf')
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        i+=1
print(largest)
# T.C - O(N)
# S.C - O(1)



# Question 2 :- find the Second largest element in an array with sorting
from array import *
a= array('i',[45,89,21,63,52,74,85,25])

sorted_array = sorted(a)
sec_larg = sorted_array[-2]
print('Second largest array : ',sec_larg)
# T.C - O(NlogN)
# S.C - O(1)

 
# Question 3 :- find the Second largest element in an array without sorting
# Method 1 in 2 pass
from array import *
a= array('i',[45,89,21,63,52,74,85,25])

largest = max(a)
sec_larg = float('-inf')
for i in range(len(a)):
    if a[i] > sec_larg and a[i] != largest:
        sec_larg = a[i]     
print('Second largest :- ',sec_larg)
# T.C - O(N+N) == O(N) but 2 pass
# S.C - O(1)

# Method 2 in Single pass 
from array import *
a= array('i',[45,89,21,63,52,74,85,25])

largest = float('-inf')
sec_larg = float('-inf')
for i in range(len(a)):
    if a[i] > largest:
        sec_larg = largest
        largest = a[i]
    elif a[i] > sec_larg and a[i] != largest:
        sec_larg = a[i]     
print(sec_larg)
# T.C - O(N) in 1 pass
# S.C - O(1)



# Question 4 :- Check if the array is sorted
from array import *
a= array('i',[10,20,30,40,50])

for i in range(0,len(a)-1):
    if a[i] > a[i+1]:
        print('Array is not sorted')
        break   
else:
    print('array is sorted')
# T.C - O(N)
# S.C - O(1)




# Question 5 :- Remove duplicates from sorted array
from array import *
a= array('i',[10,20,25,25,30,30,40,40,50,60,60])
i=0
for j in range(i+1,len(a)):
    if a[j] != a[i]:
        i+=1
        a[i],a[j] = a[j],a[i]

del(a[i+1:])
print("After removing duplicate array : ",a)
# T.C - O(N)
# S.C - O(1)