##############################################
# Title: Algorithm Analysis (MA4)
# Author: Rhea Toves
# Version: 1.0
# Date: February 11, 2022
#
# Description: This program walks through the five
# python problems listed in the assignment. Working with
# time complexity, algorithmic efficiency, and more.
##############################################

'''
Problem 1
1. 1000/250 = n/20 --> therefore, n = 80 seconds
2. (1000 * log(1000))/(250 * log(250)) = n/20 --> therefore, n = 100.08 seconds
3. (1000^3)/(250^3) = n/20 --> therefore, n = 1280 seconds
4. (2^1000)/(2^250) = n/20 --> therefore, n = 1.1844e seconds

Problem 2
def f(n):
    if n <= 0:
        return 0
    return 1 + f(n - 1)

def g(n):
    summ = 0
    for i in range(0, n, 1):
        summ += 1
    return summ

1. The runtime complexity of f(n) = O(N) and g(n) = O(N).
2. The memory complexity for f(n) = O(N) and g(n) = O(1).
3. BELOW: Write another function called h(n) that does the same thing, but is significantly faster.

'''

# Problem 2, number 3
def h(n):
    return n * (n-1) / 2

'''
Problem 3
def f(n):
   if n <= 1:`
      return 1
   return 1 + f(n/2)

def g(n):
   i = 1
   while i < n:
       f(i)
       i *= 2
       
--> The function, g(n), is logarithmic because the greater the input size, the function operates the same
way, but slower. Therefore, the runtime complexity for g(n) = O(log(N)).
       
Problem 4
1. Determining whether or not a number exists in a list.
Pseudo code/thought process

for i in a:
    if i == n:
        return True
    else:
        return False
    
--> This function is linear, looking through a list of numbers and having the singular task
of determining whether or not a number exists in a list so therefore, the algorithmic efficiency = O(N)

2. Finding the smallest number in a list.
Pseudo code/thought process

for i in range(1, n):
    if a[i] < min:
        return i
    else:
        continuing running until the smallest number is found

--> This function is linear, looking through a list of numbers and having the singular task
of finding the smallest number so therefore, the algorithmic efficiency = O(N)

3. Determining whether or not two unsorted lists of the same length contain all of the same values.
Pseudo code/thought process

for i in range(0, n):
    for j in range(0, n):
        if a[i] == b[j]:
            return True
        else:
            return False

--> This function is quadratic, comparing two elements (length and values) this function would need
a for loop inside of another for loop so therefore, the algorithmic efficiency = O(N^2)

4. Determining whether or not two sorted list contain all of the same values.
Pseudo code/thought process

for i in range(0, n):
    if a[i] == b[i]:
        return True
    else:
        return False

--> This function is linear, comparing two lists and determining matching values would take one for loop
and there is one task at hand so therefore, the algorithmic efficiency = O(N)

'''

# Problem 5
import numpy as np
import random
import time

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def main():
    for N in [int(1000), int(10000), int(100000), int(1000000), int(10000000)]:
        array = np.arange(1, N+1)
        target = random.randint(int(N/4), int(3*(N/4)))

        start_time = time.time()
        result = linear_search(array, target)
        end_time = time.time()
        computation_time = end_time - start_time

        print("Input array size: ", N)
        print("Search result: ", result)
        print("Search computation time: ", computation_time, "seconds")

main()

