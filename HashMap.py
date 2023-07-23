# TWO SUM PROBLEM

nums = [1,3,4,9]
target = 12


def twoSum(nums,target):
  prevMap = {}
  for index,number in enumerate(nums):
    diff = target-number
    if diff in prevMap:
      return [prevMap[diff],index]
    prevMap[number] = index

result = twoSum(nums,target)
print(result)