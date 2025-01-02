class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initialize an empty dictionary to store the numbers from nums 
        # as keys and their corresponding indices as values
        num_dict = {}
        # iterate through the loop using the range of the nums list
        for current_index in range(len(nums)):
            # for each number in nums
            # calculate the difference between target and the current number
            # store this in a variable called complement
            complement = target - nums[current_index]
            # check if the complement exists in the num_dict dictionary
            if complement in num_dict:
                # if so, return the list containing the index of current
                # and the index of the complement
                return[num_dict[complement], current_index]
            # otherwise if complement doesn't exist to fulfill the target
            # add the current number value -> nums[current_index]
            # and add the current number's index -> current_index
            # to the dictionary storing indices  -> num_dict
            num_dict[nums[current_index]] = current_index
        # if there was no guarantee that there is exactly one solution,
        # make sure to return an empty list at the end if no solution is found
        # return []
