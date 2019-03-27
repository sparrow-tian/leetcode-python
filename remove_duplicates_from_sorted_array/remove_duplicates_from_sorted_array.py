class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        while True:
            if len(nums)>(k+1):
                
                if nums[k]==nums[k+1]:
                    nums.pop(k+1)
                else:
                    k=k+1
            else:
                break
        return len(nums)
