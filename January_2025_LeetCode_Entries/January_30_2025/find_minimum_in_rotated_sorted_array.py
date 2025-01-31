# pseudocode

def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            # The minimum is in the right half
            left = mid + 1
        else:
            # The minimum is in the left half (including mid)
            right = mid
    
    return nums[left]
    