# Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

def numberOfOdd(a,b):
  if(b%2 == 1):
    return (b-a)//2 + 1
  elif(b%2 == 0):
    return (b-a)//2

print("No of Odd Numbers in Range(3,7)",numberOfOdd(3,7))
print("No of Odd Numbers in Range(8,10)",numberOfOdd(8,10))
print("No of Odd Numbers in Range(4,9)",numberOfOdd(4,9))