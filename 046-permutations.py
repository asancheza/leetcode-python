#!/usr/bin/python
# -*- coding: utf-8 -*-

def _permute(result, cur, num):
  if len(cur) == len(num):
    result.append(cur)
  else:
    for i in xrange(len(num)):
      if num[i] not in cur:
        _permute(result, cur + [ num[i] ], num)

def permute(num):
  result = []
  _permute(result, [], num)
  return result

print permute(['1','2','3'])


