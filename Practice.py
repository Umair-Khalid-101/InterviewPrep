"""
  The function reverseArray takes in a list of numbers and returns a new list with the numbers in
  reverse order.
  
  :param numbers: The parameter "numbers" is a list of integers
  :return: a reversed version of the input array.
"""

# def reverseArray(numbers):
#   reverse = []
#   for number in range(len(numbers)-1,-1,-1):
#     reversednum = numbers[number]
#     reverse.append(reversednum)
#   return reverse
    
# print(reverseArray([1,4,3,2]))


"""
  The above code implements a binary search algorithm to find the index of a given element in a sorted
  array.
  
  :param array: The array parameter is a list of strings containing names
  :param search: The "search" parameter is the element that you want to search for in the array
  :return: The binarySearch function returns the index of the element if it is found in the array, and
  None if the element is not found.
"""
# BINARY SEARCH

# array = ["Ali","Haseeb","Ibrahim","Zohaib","Saad","Zain","Ansab","Umair"]

# def binarySearch(array, search):
#   low = 0
#   high = len(array)-1
#   while low <= high:
#     mid = (low + high)//2
#     guess = array[mid]
#     if guess == search:
#       return mid
#     if guess > search:
#       high = mid - 1
#     else:
#       low = mid + 1
#   return None 


# guess = input("Enter Guess: ")
# print("Sorted: ",sorted(array))
# print (binarySearch(sorted(array), guess))


"""
  The code implements the selection sort algorithm to sort an array in ascending order.
  
  :param array: The array parameter is a list of integers
  :return: The selectionSort function returns a sorted array in ascending order.
"""

# array = [3,5,1,4,6,8]

# def findSmallest(array):
#   smallest = array[0]
#   smallest_index = 0
#   for i in range(len(array)-1):
#     if array[i] < smallest:
#       smallest = array[i]
#       smallest_index = i
#   return smallest_index

# def selectionSort(array):
#   sortedArray = []
#   for i in range(len(array)-1):
#     smallest = findSmallest(array)
#     sortedArray.append(array.pop(smallest))
#   return sortedArray

# print(selectionSort(array))

