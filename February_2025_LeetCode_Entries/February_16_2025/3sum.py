class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # starting with sorting the array to help
        # remove duplicates easily
        nums.sort()
        # initialize empty results list to store
        # the eventual triplets
        result = []
        
        for i in range(len(nums) - 2):
            # stop at len(nums) - 2 because 3 numbers are needed
            if i > 0 and nums[i] == nums[i - 1]:
                # skip duplicate values for nums[i]
                continue
            # using two pointers to find the other two numbers
            # left starts right after i
            left = i + 1
            # right starts at the end
            right = len(nums) - 1

            while left < right:
                # calculate sum of the three numbers
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # if the triplet is valid
                    # add it to the results list
                    result.append([nums[i], nums[left], nums[right]])

                    # move both pointers to look for more triplets
                    left += 1
                    right -= 1

                    # skip duplicate values for left and right
                    # to avoid repeating triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                # if the sum is too small
                elif total < 0:
                    # move the left pointer to a larger number
                    left += 1
                # if the sum is too large
                else:
                    # move the right pointer to a smaller number
                    right -= 1
        return result
        