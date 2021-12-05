#!/usr/bin/env python3
import sys

print("This is the name of the program:",
       sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-1))
print("Argument List:",
       str(sys.argv))
       

add = 0.0
  
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add)
