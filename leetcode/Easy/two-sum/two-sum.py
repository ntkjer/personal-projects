class Solution(object):
	#O(n) solution
	def twoSum(self, nums, target):
    	dict = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if dict.get(complement) is not None:
                return [dict[complement], i]
			dict[nums[i]] = i
		raise ValueError("No solution")
