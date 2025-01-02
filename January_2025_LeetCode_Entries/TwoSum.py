class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initialize an empty dictionary to store the visited indices
        num_indices = {}
        # iterate through the loop using the range of the nums list
        for current_index in range(len(nums)):
            # for each number in nums
            # calculate the difference between target and the current number
            # store this in a variable called variable_x
            variable_x = target - nums[current_index]
            # check if variable_x exists in the nums_indices dictionary
            if variable_x in num_indices:
                # if so, return the list containing the index of current
                # and the index of variable_x
                return[num_indices[variable_x], current_index]
            # otherwise if variable_x doesn't exist to fulfill the target
            # add the current number value -> nums[current_index]
            # and add the current number's index -> current_index
            # to the dictionary storing indices  -> num_indices
            num_indices[nums[current_index]] = current_index
