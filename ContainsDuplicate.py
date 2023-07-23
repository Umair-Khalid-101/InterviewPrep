# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

nums1= [1,1,2,3,3]
nums2= [1,2,3,4]

def containsDuplicate(numbers):
  hashSet = set()
  
  for n in numbers:
    if n in hashSet:
      return True
    hashSet.add(n)
  return False

result1 = containsDuplicate(nums1)
result2 = containsDuplicate(nums2)
print(result1)
print(result2)