# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

numbers1 = [3,7,-4,3,2,6,-3]
numbers2 = [5,4,-1,7,8]
numbers3 = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(numbers):
  maxSubArray = numbers[0]
  currentSum = 0
  
  for n in numbers:
    if(currentSum < 0):
      currentSum = 0
    currentSum += n
    maxSubArray = max(maxSubArray,currentSum)
    
  return maxSubArray

result1 = maxSubArray(numbers1)
result2 = maxSubArray(numbers2)
result3 = maxSubArray(numbers3)
print(result1)
print(result2)
print(result3)