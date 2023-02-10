# Average Salary Excluding the Minimum and Maximum Salary
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

def average(salary):
    salary.remove(max(salary))
    salary.remove(min(salary))
    a = len(salary)
    total = 0
    for i in range(a):
      total = total + salary[i]
    return total/a

salary = [4000,7000,1000,9000]
print("Average of Salries excluding Max Salary and Min Salary is: ",average(salary))