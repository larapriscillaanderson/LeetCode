class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. Sort the array to handle duplicates
        nums.sort()
        result = []

        # 2. Loop through the array with index i (first number)
        for i in range(len(nums) - 3):  
        # Stop at len(nums) - 3 
        # because we need at least 4 elements
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicates for i  
                continue

            # 3. Loop through the array with index j (second number)
            for j in range(i + 1, len(nums) - 2):  
                # Stop at len(nums) - 2 for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:  
                    # Skip duplicates for j
                    continue

                # 4. Use two pointers (left, right) to find two more numbers
                left, right = j + 1, len(nums) - 1
                while left < right:
                    # a. Calculate sum of nums[i], nums[j], nums[left], 
                    # and nums[right]
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                
                    # b. If the sum matches the target, store the quadruplet
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # c. Move left and right pointers while skipping duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move the pointers
                        left += 1
                        right -= 1

                    # d. If sum is too small, move left pointer to increase sum
                    elif total < target:
                        left += 1

                    # e. If sum is too large, move right pointer to decrease sum
                    else:
                        right -= 1

        # 5. Return the list of unique quadruplets
        return result
        