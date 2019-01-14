class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,value in enumerate(nums):
            new=target-value
            if new in d.keys():
                return [d[new],i]
            d[value]=i
