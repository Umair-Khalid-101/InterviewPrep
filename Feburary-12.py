# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def my_function(nums,target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[j] == target - nums[i]:
        return print([i,j])
    

nums = [3,2,4]
target = 6
my_function(nums,target)