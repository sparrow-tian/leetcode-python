class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[slow]=nums[i] 
                slow+=1
        return slow
