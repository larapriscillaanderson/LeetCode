"""def threeSum(nums):
    sort nums
    result = []
    
    for i from 0 to len(nums) - 2:
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            
            if sum == 0:
                add [nums[i], nums[left], nums[right]] to result
                move left and right to avoid duplicates
            elif sum < 0:
                left += 1
            else:
                right -= 1
    
    return result"""
