#!/usr/bin/python

def combination(nums):
  if len(nums) == 0:
    return ""

  result = []
  lenght = len(nums)

  _combination(nums, [], result, lenght)
  return result

def _combination(nums, res, result, lenght):
  if len(res) == lenght:
    result.append(res)
    return

  for i in nums:
    _combination(nums[1:], res + [i], result, lenght)

def check_sum(nums, target):
  res = combination(nums)
  result = []

  for num in res:
    sum = 0
    numbers = []
    
    for n in num:
      sum += int(n)
      numbers.append(n)

      if sum  == target:
        if numbers not in result:
          result.append(numbers)
        break

  return result

print check_sum([1,2,2,3,2], 7)