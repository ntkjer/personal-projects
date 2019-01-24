class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)-1):
            j = 0
            if nums[i] == nums[j]:
                nums.remove(nums[i])
            else:
                j += 1
        return len(nums)

        