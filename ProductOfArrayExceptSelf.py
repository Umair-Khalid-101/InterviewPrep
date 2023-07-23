# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

numbers1 = [1,2,3,5]
numbers2 = [-1,1,0,-3,5,-5]

def productExceptSelf(numbers):
  result = [1] * (len(numbers))
  
  # prefix
  prefix = 1
  for i in range(len(numbers)):
    result[i] = prefix
    prefix *= numbers[i]
    
  print("Prefix Array: ", result) 
  
  #postfix
  postfix = 1
  for i in range(len(numbers)-1,-1,-1):
    result[i] *= postfix
    postfix *= numbers[i]
    
  print("Postfix Array: ", result)
  return result
  
productExceptSelf(numbers1)