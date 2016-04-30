#!/usr/bin/python
# *-* coding: utf-8 *-*

# Tip: product[i] = products_left_i * products_right_i. 
# Ex: 1 2 3 4
# Left of 2 : 1
# Right of 2: 12
# Product of 2: 12

def product(nums):
  before = [0] * len(nums)
  after = [0] * len(nums)
  product = [0] * len(nums)

  before[0] = 1
  for i in xrange(1, len(nums)):
  	print i, before[i], before[i-1], nums[i-1] 
  	before[i] = before[i-1] * nums[i-1]

  after[len(nums) - 1] = 1
  for i in reversed(xrange(len(nums) - 1)):
  	after[i] = after[i+1] * nums[i+1]

  for i in xrange(0, len(nums)):
  	product[i] = after[i] * before[i]

  return product

print product([1,2,3,4])