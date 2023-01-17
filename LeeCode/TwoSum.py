
from typing import Self


class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i
    print(twoSum(Self, nums = [3,3], target = 6))