class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize a dictionary to track counts
        count_map = {}
        # create threshold limit for counting
        # the majority element must appear more than this value
        n = len(nums) // 3
        # iterate through each number using a for loop
        for num in nums:
            # if num is already in count_map, increment by 1
            # if not, then initialize its count by setting it to 0
            # then add 1
            count_map[num] = count_map.get(num, 0) + 1
            # collect elements that appear more than n // 3 times
            result = []
            for key, val in count_map.items():
                # if the count of an element appears more than n // 3
                # times, then it is added to the results list
                if val > n:
                    result.append(key)
        # return the list of majority elements
        return result
        