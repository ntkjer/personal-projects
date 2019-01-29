class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        p_1 = p_2 = 0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = []
        while True:
            try:
                if nums1[p_1] > nums2[p_2]:
                    p_2 += 1
                elif nums1[p_1] < nums2[p_2]:
                    p_1 += 1
                else:
                    res.append(nums1[p_1])
                    p_1 += 1
                    p_2 += 1
            except IndexError:
                break
                
        return res
    
            