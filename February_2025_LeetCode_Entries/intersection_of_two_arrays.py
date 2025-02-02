class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # convert nums1 into a set for ease of lookup
        set1 = set(nums1)
        result = set()

        # iterate through nums2 and check if it's in set1
        for num in nums2:
            # check if the desired shared number is in the first set
            if num in set1:
                # if so, add it to the results set for storage
                # this will also accomplish avoiding duplicates
                result.add(num)
        # at the end, must return the result set back into list form
        return list(result)
        