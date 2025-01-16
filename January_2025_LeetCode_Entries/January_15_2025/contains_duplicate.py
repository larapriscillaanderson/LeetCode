class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create empty hash set to store numbers as they're seen
        seen = set()
        # check if each number exists in the hash set seen
        for element in nums:
            if element in seen:
                # if a duplicate is found
                return True
            # otherwise if not found, add num to seen
            seen.add(element)
        return False
        