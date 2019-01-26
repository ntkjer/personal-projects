class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniques = set()
        found_duplicate = False
        for num in nums:
            if num not in uniques:
                uniques.add(num)
            else:
                found_duplicate = True
        return found_duplicate
        