# Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

import math

def numberOfOdd(low,high):
  if(high%2 == 1):
    return (high-low)//2 + 1
  elif(high%2 == 0):
    return int(math.ceil((high-low)/2))

print("No of Odd Numbers in Range(3,7)",numberOfOdd(3,7))
print("No of Odd Numbers in Range(8,10)",numberOfOdd(8,10))
print("No of Odd Numbers in Range(4,9)",numberOfOdd(4,9))
print("No of Odd Numbers in Range(21,22)",numberOfOdd(21,22))