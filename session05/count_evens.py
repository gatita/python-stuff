#!/usr/bin/env python

def count_evens(nums):
    return len([x for x in nums if not x % 2])

nums = [2, 1, 2, 3, 4]

print count_evens(nums)